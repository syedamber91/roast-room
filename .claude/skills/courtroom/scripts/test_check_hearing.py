import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
spec = importlib.util.spec_from_file_location("chk", HERE / "check_hearing.py")
chk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chk)

QUOTE = "we will open three plants by march 2027 as planned"
OTHER_QUOTE = "we will close the old line in june 2027 as agreed"
CASE_BOOK = "Revenue 43,360 in the quarter ended 2026-06-30. Debt 148,246 at 2026-03-31."
EXTERNAL = "## E001\nSteel prices, source and date.\n"

GOOD = f"""# Hearing: TEST

## I3 Guidance
### Q1 Lawyer
TO: the convict
QUESTION: What revenue was filed for the quarter ended 2026-06-30, and on which date was the plant plan last stated?
WHY I ASK: Q1.1, did last quarter's guidance hold
IF DEFLECTED: Give the number and the date.

### A1 Convict
ANSWER: As of 2026-10-30 the filed revenue for the quarter ended 2026-06-30 was 43,360 million (S026, PDF page 7), and the plant plan was stated on 2026-05-08.
MOVE: cite
EVIDENCE:
- "{QUOTE}" (S001, Jane Roe, held 2026-05-08)
- filed revenue from operations 43,360 million (S026, quarter ended 2026-06-30)
STATE I CLAIM: answered
WHAT WOULD SETTLE IT: nothing further

### Judge note
STORY SO FAR:
1. Revenue was 43,360 million in the quarter ended 2026-06-30 (case book; hearing I3 A1).
2. The plant plan was stated on 2026-05-08 (hearing I3 A1, S001).
I DID NOT UNDERSTAND:
- What "filed" means for a number, because the case book does not say.
STATE PROPOSED: Q1 answered, because it has a number and a date.
"""


def make_brains(tmp_path):
    convict, lawyer = tmp_path / "convict", tmp_path / "lawyer"
    convict.mkdir(exist_ok=True)
    lawyer.mkdir(exist_ok=True)
    (convict / "sources.md").write_text("- S001 | A call by Jane Roe | https://x | 2026-05-08 | n/a\n- S026 | An annual report, filed tables, not management speech | https://x | 2026-03-31 | n/a\n", encoding="utf-8")
    (convict / "calls.md").write_text(f'Jane said: "{QUOTE}" and later "{OTHER_QUOTE}".', encoding="utf-8")
    (lawyer / "questions.md").write_text("### Q1.1 Did last quarter's guidance hold?\n", encoding="utf-8")
    return convict, lawyer


def run(tmp_path, hearing, external=""):
    convict, lawyer = make_brains(tmp_path)
    return chk.check(hearing, CASE_BOOK, convict, lawyer, external)


def guards(problems, severity="FAIL"):
    return {p.guard for p in problems if p.severity == severity}


def test_a_clean_hearing_has_no_problems(tmp_path):
    assert [str(p) for p in run(tmp_path, GOOD, EXTERNAL)] == []


def test_each_guard_catches_its_planted_failure(tmp_path):
    plants = {
        "quote-source": GOOD.replace(QUOTE, "we will open nine plants by march 2027 as planned"),                      # an invented quote
        "turn-shape": GOOD.replace("STATE I CLAIM: answered\n", ""),                                                   # a missing field
        "id-exists": GOOD.replace("(S001, Jane Roe", "(S999, Jane Roe"),                                               # an id the brain does not have
        "no-speech-id": GOOD.replace('"' + QUOTE + '" (S001, Jane Roe, held 2026-05-08)', '"' + QUOTE + '" (S026, PDF page 7, year to 2026-03-31)'),   # a quote behind a filed-tables id
        "has-evidence": GOOD.replace("(S026, PDF page 7)", "").replace("(S001, Jane Roe, held 2026-05-08)", "").replace("(S026, quarter ended 2026-06-30)", "").replace("S001, ", ""),
        "number-date": GOOD.replace("ANSWER: As of 2026-10-30", "ANSWER: The capex was 4,500 million for the plants and nobody knows more than that at all and so on and on and so on and on, and as of 2026-10-30"),
        "lawyer-number": GOOD.replace("QUESTION: What revenue", "QUESTION: Why was the 7,777 million figure used, and what revenue"),
        "judge-story": GOOD.replace("2. The plant plan was stated on 2026-05-08 (hearing I3 A1, S001).", "2. The company is doing well."),
        "external-id": GOOD.replace("- filed revenue from operations 43,360 million (S026, quarter ended 2026-06-30)", "- the plant cost 4,500 million (E001, held 2026-10-01)"),
    }
    for guard, hearing in plants.items():
        assert guard in guards(run(tmp_path, hearing, EXTERNAL)), f"{guard} did not catch its plant"


def test_a_lawyer_who_quotes_the_convict_is_fine_and_a_judge_who_quotes_a_brain_is_caught(tmp_path):
    q2 = f'### Q2 Lawyer\nTO: the convict\nQUESTION: You said "{QUOTE}", so on which date was it first said?\nWHY I ASK: Q1.1, one line\nIF DEFLECTED: Give the date.\n'
    assert guards(run(tmp_path, GOOD + "\n" + q2, EXTERNAL)) == set()                       # after the convict spoke, the lawyer may quote the convict
    before = GOOD.replace("QUESTION: What revenue", f'QUESTION: You said "{QUOTE}", so what revenue')
    assert "quote-source" in guards(run(tmp_path, before, EXTERNAL))                        # before the convict spoke, it may not
    judge_quotes_brain = GOOD.replace("I DID NOT UNDERSTAND:", f'I DID NOT UNDERSTAND:\n- The line "{OTHER_QUOTE}" is odd, because it is quoted.')
    assert "quote-source" in guards(run(tmp_path, judge_quotes_brain, EXTERNAL))


def test_a_bare_none_in_i_did_not_understand_is_caught_and_a_reasoned_none_is_not(tmp_path):
    bare = GOOD.replace('- What "filed" means for a number, because the case book does not say.', "none")
    reasoned = GOOD.replace('- What "filed" means for a number, because the case book does not say.', "none, because every term was defined in the case book")
    assert "judge-story" in guards(run(tmp_path, bare, EXTERNAL))
    assert guards(run(tmp_path, reasoned, EXTERNAL)) == set()


def test_an_external_id_is_allowed_on_an_external_baseline_line_only(tmp_path):
    baseline = "## Baseline\n### Convict baseline 3\nB19 ANSWER: steel is dearer (E001, held 2026-10-01) | MOVE: cite | STATE I CLAIM: partial\nB07 ANSWER: profit fell (E001, held 2026-10-01) | MOVE: cite\n"
    problems = [p for p in run(tmp_path, baseline, EXTERNAL) if p.guard == "external-id"]
    assert len(problems) == 1 and "B07" in problems[0].message


def test_the_real_trial_hearing_is_flagged_where_the_trial_found_flaws_and_clean_where_the_fixes_worked():
    session = ROOT / "sessions" / "2026-10-30-court-biocon-example"
    problems = chk.check((session / "hearing.md").read_text(encoding="utf-8"), (session / "case-book.md").read_text(encoding="utf-8"),
                         ROOT / ".claude" / "skills" / "roast-room" / "brains" / "biocon-management",
                         ROOT / ".claude" / "skills" / "roast-room" / "brains" / "india-market-analyst")
    by_turn = {}
    for p in problems:
        if p.severity == "FAIL":
            by_turn.setdefault(p.turn, set()).add(p.guard)
    assert by_turn["Q1 Lawyer"] == {"turn-shape"}                                    # compound question, three-step follow-up
    assert by_turn["A1 Convict"] == {"turn-shape", "quote-source"}                   # four moves, nine evidence lines, quotes with the id first
    assert by_turn["A3 Convict"] == {"id-exists"}                                    # the placeholder S0xx
    assert by_turn["Judge note"] == {"quote-source"}                                 # a paraphrase put inside quotation marks
    assert by_turn["WA1 Convict"] == {"number-date"} and by_turn["WA2 Convict"] == {"number-date"}   # numbers with no date near them
    for clean in ("Q2 Lawyer", "A2 Convict", "Q3 Lawyer", "Judge close"):
        assert clean not in by_turn, clean                                           # every quote in A2 is verbatim and sits next to its id


def test_a_baseline_line_may_carry_its_date_anywhere_on_the_line_but_must_carry_one(tmp_path):
    ok = GOOD + "\n## Baseline\n### Convict baseline 1\nB01 ANSWER: Sales were 43,360 and profit was 8,472 and the filed record of this is long enough to push the date well past the usual window, quarter ended 2026-06-30. | MOVE: cite | EVIDENCE: x | STATE I CLAIM: answered | WHAT WOULD SETTLE IT: nothing\n"
    bad = ok.replace(", quarter ended 2026-06-30", "")
    assert "number-date" not in guards(run(tmp_path, ok, EXTERNAL))
    assert "number-date" in guards(run(tmp_path, bad, EXTERNAL))


def test_a_move_line_may_use_a_pipe_between_two_moves_but_not_three(tmp_path):
    two = GOOD.replace("MOVE: cite", "MOVE: cite | mitigate")
    three = GOOD.replace("MOVE: cite", "MOVE: cite | mitigate | concede")
    assert "turn-shape" not in guards(run(tmp_path, two, EXTERNAL))
    assert "turn-shape" in guards(run(tmp_path, three, EXTERNAL))
