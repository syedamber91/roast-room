import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("rules", HERE / "court_rules.py")
r = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r)


# ---- ceilings

def test_all_answered_gives_three():
    assert r.section_ceiling({"Q1.1": "answered", "Q1.2": "answered"}, ["Q1.1"])[0] == 3


def test_decisive_answered_but_another_slipped_gives_two_and_names_it():
    c, why = r.section_ceiling({"Q1.1": "answered", "Q1.2": "partial"}, ["Q1.1"])
    assert c == 2 and "Q1.2" in why


def test_decisive_partial_gives_one():
    assert r.section_ceiling({"Q1.1": "partial", "Q1.2": "answered"}, ["Q1.1"])[0] == 1


def test_decisive_no_data_deflected_or_unverified_give_zero():
    for st in ("no data", "deflected", "unverified"):
        assert r.section_ceiling({"Q1.1": st}, ["Q1.1"])[0] == 0


def test_decisive_not_heard_gives_zero_and_says_so():
    c, why = r.section_ceiling({"Q1.2": "answered"}, ["Q1.1"])
    assert c == 0 and "Q1.1" in why and "not heard" in why


def test_no_guidance_special_case_sets_two_with_anchor_and_one_without():
    assert r.section_ceiling({"Q1.1": "no data"}, ["Q1.1"], no_guidance="numeric")[0] == 2
    assert r.section_ceiling({"Q1.1": "no data"}, ["Q1.1"], no_guidance="none")[0] == 1


def test_no_guidance_special_case_cannot_lift_above_two():
    assert r.section_ceiling({"Q1.1": "answered"}, ["Q1.1"], no_guidance="numeric")[0] == 2


def test_disputed_question_counts_at_the_lower_reading():
    assert r.lowest_state(["answered", "partial"]) == "partial"
    assert r.lowest_state(["partial", "no data"]) == "no data"


# ---- cutting the judge down

def test_judge_above_ceiling_is_cut_and_the_sentence_is_printed():
    rows = r.cap_scores({"S1": 3}, {"S1": (2, "Q1.2 was not")})
    s1 = rows[0]
    assert s1["final"] == 2 and s1["cut"] == "judge said 3, evidence allows 2, because Q1.2 was not"


def test_judge_below_ceiling_is_kept():
    rows = r.cap_scores({"S1": 1}, {"S1": (2, "x")})
    assert rows[0]["final"] == 1 and rows[0]["cut"] is None


def test_a_section_the_judge_did_not_score_counts_zero_and_says_so():
    rows = r.cap_scores({}, {})
    assert rows[3]["final"] == 0 and "no number" in rows[3]["note"]
    assert len(rows) == 7


# ---- bands and total

def test_bands_cover_every_total_from_zero_to_twenty_one_once():
    for t in range(22):
        assert r.band_of(t)["caveat"] == r.BAND_CAVEAT
    assert r.band_of(18)["range"] == "18 to 21" and r.band_of(12)["range"] == "12 to 17"
    assert r.band_of(7)["range"] == "7 to 11" and r.band_of(6)["range"] == "0 to 6"


# ---- position

def test_hard_gate_forces_avoid_whatever_the_trust():
    assert r.compute_position(21, ["G-C"], True, True)[0] == "avoid"


def test_g_e_caps_at_wait_even_with_top_trust():
    assert r.compute_position(21, ["G-E"], True, True)[0] == "wait"


def test_buy_needs_band_price_and_results():
    assert r.compute_position(18, [], True, True)[0] == "buy"
    assert r.compute_position(17, [], True, True)[0] == "wait"
    assert r.compute_position(18, [], False, True)[0] == "wait_good"
    assert r.compute_position(18, [], True, False)[0] == "wait_good"


def test_wait_good_needs_trust_twelve_or_more_and_missing_price_or_results():
    assert r.compute_position(12, [], False, True)[0] == "wait_good"
    assert r.compute_position(11, [], False, True)[0] == "wait"


def test_low_trust_is_wait_not_avoid():
    key, why = r.compute_position(3, [], True, True)
    assert key == "wait" and "below the 18 to 21 band" in why[0]


def test_judge_can_move_down_never_up():
    assert r.apply_judge_position("wait", "avoid")[0] == "avoid"
    key, note = r.apply_judge_position("wait", "buy")
    assert key == "wait" and "rule's position stands" in note
    assert r.apply_judge_position("wait_good", "wait")[0] == "wait"
    assert r.apply_judge_position("wait", None) == ("wait", None)


def test_reader_line_buy_only_when_position_is_buy():
    assert r.reader_line_problems("wait", "Buy") != []
    assert r.reader_line_problems("buy", "Buy") == []
    assert r.reader_line_problems("avoid", "Wait") != []
    assert r.reader_line_problems("wait", "Wait: trust good, entry not yet") == []


# ---- final turn

FINAL = """### Judge final

SECTION SCORES:
- S1 | 2 | states: Q1.1 no data, Q1.2 partial | WHY: no group guide, segment numbers exist.
- S2 | 1 | states: Q2.1 partial | WHY: words, no number.
DIRECTION: mixed
DIRECTION WHY: profit rose in four quarters and fell in one (hearing I1 A1).
RED FLAGS:
- Q1.1 | no group guide | hearing I3 A1
POSITION: Wait | REASON: the rule gives Wait.
READER NOT OWN: Wait | what would change it: a filed quarter with margin above 20%.
READER OWN: hold and watch | what would change it: a covenant breach.
TRIGGERS:
1. next filed quarter | check: operating margin against 19.5% | moves: up
2. covenant test at 2026-09-30 | check: thresholds | moves: down
NOT DECIDED:
- price against value
- anything after 2026-10-29
STORYLINE:
1. Biocon sells medicines (case book s2).
2. Profit fell, not in the record why.
GLOSSARY:
- Biosimilar: a close copy of a medicine made from living cells.
WHY THE DEFENCE HELD OR DID NOT: it held on filed numbers and slipped on guidance (hearing I3 A1).
"""


def test_parse_final_reads_every_part():
    f = r.parse_final(FINAL)
    assert f["scores"] == {"S1": 2, "S2": 1}
    assert f["states"]["S1"] == {"Q1.1": "no data", "Q1.2": "partial"}
    assert f["direction"] == "mixed" and f["position"] == "wait"
    assert f["reader_not_own"][0] == "Wait" and f["reader_own"][0] == "hold and watch"
    assert [t["moves"] for t in f["triggers"]] == ["up", "down"]
    assert len(f["storyline"]) == 2 and f["glossary"][0]["term"] == "Biosimilar"
    assert f["red_flags"][0]["question"] == "Q1.1" and f["missing"] == []


def test_parse_final_reports_what_is_missing_instead_of_guessing():
    f = r.parse_final("SECTION SCORES:\n- S1 | 2 | states: Q1.1 answered | WHY: x\n")
    assert "POSITION" in f["missing"] and f["position"] is None and f["direction"] is None


def test_unknown_direction_word_is_not_accepted():
    assert r.parse_final("DIRECTION: great\n")["direction"] is None


# ---- the judge-final wording must spell out the ceiling rule (T2: S1 and S5 stability)

PROMPTS = HERE.parent / "references" / "hearing-prompts.md"


def _judge_final_text():
    text = PROMPTS.read_text()
    start = text.index("\n## Judge final\n")
    nxt = text.find("\n## ", start + 5)
    return text[start:nxt if nxt != -1 else len(text)]


def test_judge_final_spells_out_the_ceiling_ladder():
    t = _judge_final_text()
    for line in ("decisive question answered and every other question answered: 3",
                 "decisive question answered but another question not answered: 2",
                 "decisive question partial: 1",
                 "decisive question no data, deflected, unverified or not heard: 0"):
        assert line in t


def test_judge_final_says_the_score_is_the_ceiling_unless_why_gives_a_reason():
    t = _judge_final_text()
    assert "Your score is the ceiling" in t and "only if WHY" in t


def test_judge_final_spells_out_the_s1_no_guidance_case():
    t = _judge_final_text()
    assert "no-guidance" in t
    assert "2 when the company gives another numeric anchor, 1 when it gives none, whatever the states say" in t
    assert "S1 no-guidance case" in t   # the Chair line that hands the judge the case


def test_judge_final_defines_partial_and_no_data_apart():
    t = _judge_final_text()
    assert "partial = words but no number" in t
    assert "no data = nothing in the record on that point" in t
    assert "List each question id once" in t


def test_judge_final_wording_matches_the_code_for_the_two_unstable_sections():
    # S1: decisive only partial, no-guidance numeric -> 2; none -> 1
    assert r.section_ceiling({"Q1.1": "partial"}, ["Q1.1"], no_guidance="numeric")[0] == 2
    assert r.section_ceiling({"Q1.1": "partial"}, ["Q1.1"], no_guidance="none")[0] == 1
    # S5: decisive no data -> 0, decisive partial -> 1
    assert r.section_ceiling({"Q5.3": "no data", "Q5.2": "partial"}, ["Q5.3"])[0] == 0
    assert r.section_ceiling({"Q5.3": "partial", "Q5.2": "partial"}, ["Q5.3"])[0] == 1


def test_judge_final_has_no_em_dash():
    assert "—" not in _judge_final_text()
