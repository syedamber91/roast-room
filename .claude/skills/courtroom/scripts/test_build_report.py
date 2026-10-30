import importlib.util
import json
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
EXAMPLE = ROOT / "sessions" / "2026-10-30-court-biocon-example"

spec = importlib.util.spec_from_file_location("rep", HERE / "build_report.py")
rep = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rep)

# A test fixture, not a judgment of BIOCON: the I3-only trial hearing plus a made-up final turn.
FINAL = """

## Judge final

### Judge final

SECTION SCORES:
- S1 | {s1} | states: Q1.1 no data, Q1.2 no data | WHY: fixture.
- S2 | 0 | states: none | WHY: no data, not heard
- S3 | 0 | states: none | WHY: no data, not heard
- S4 | 0 | states: none | WHY: no data, not heard
- S5 | 0 | states: none | WHY: no data, not heard
- S6 | 0 | states: none | WHY: no data, not heard
- S7 | 0 | states: none | WHY: no data, not heard
DIRECTION: can't tell
DIRECTION WHY: one issue heard (hearing I3 A1).
RED FLAGS:
- Q1.1 | no group guide | hearing I3 A1
POSITION: {position} | REASON: fixture.
READER NOT OWN: {not_own} | what would change it: more hearing.
READER OWN: hold and watch | what would change it: a breach.
TRIGGERS:
1. next filed quarter | check: margin | moves: up
NOT DECIDED:
- price against value
STORYLINE:
{story}
GLOSSARY:
- Margin: what is left of each 100 rupees of sales.
WHY THE DEFENCE HELD OR DID NOT: it held on filed numbers (hearing I3 A1).
"""
STORY = "\n".join("%d. A line about the case (case book s3)." % i for i in range(1, 11))


def session(tmp_path, s1=3, position="Wait", not_own="Wait", story=STORY):
    dest = tmp_path / "sess"
    shutil.copytree(EXAMPLE, dest)
    with open(dest / "hearing.md", "a", encoding="utf-8") as f:
        f.write(FINAL.format(s1=s1, position=position, not_own=not_own, story=story))
    return dest


def build(dest, **kw):
    args = dict(gates=set(), price_on_file=True, results_on_file=True, no_guidance=None)
    args.update(kw)
    return rep.build(dest, **args)


def test_chart_data_is_read_from_the_real_case_book_and_brain(tmp_path):
    dash, _, _ = build(session(tmp_path))
    x = dash["exhibits"]
    assert len(x["quarters"]) == 11 and x["quarters"][-1]["rev"] == 43360 and x["quarters"][-1]["margin"] == 19.5
    assert x["quarters"][5]["gen"] == 10475 and x["quarters"][5]["third"] == 10180
    assert [b["date"] for b in x["breaks"]] == ["2025-06-30", "2026-06-30"] and x["basis_changed"] is True
    assert x["debt"]["bands"][0] == {"band": "Under 1 year", "now": 65476.0, "prev": 53498.0}
    assert x["debt"]["bands"][3]["now"] == 0.0
    assert len(x["holdings"]) == 25 and x["holdings"][-1]["promoter_pct"] == 44.68
    assert all(h["pledged"] == "false" for h in x["holdings"])
    assert x["promises"] == {"kept": 14, "missed": 5, "open": 9, "depends": 11}
    assert len(x["calls"]) == 14 and sum(c["answered"] for c in x["calls"]) == 311
    assert len(x["votes"]) == 6 and max(v["max_against"] for v in x["votes"]) == 26.40


def test_a_missing_source_gives_none_not_an_estimate():
    assert rep.debt_data("no tables here") is None
    assert rep.holdings_data("no tables here") is None
    assert rep.quarters_data("no tables here") == (None, [])
    assert rep.calls_data(Path("/nonexistent")) is None and rep.promises_data(Path("/nonexistent")) is None


def test_planted_failure_judge_score_above_its_ceiling_is_cut_and_reported(tmp_path):
    dash, problems, _ = build(session(tmp_path, s1=3))
    s1 = dash["decision"]["scores"][0]
    assert s1["judge"] == 3 and s1["final"] == 0 and s1["cut"].startswith("judge said 3, evidence allows 0")
    assert any(p.startswith("judge-ceiling: S1") for p in problems)
    assert dash["decision"]["total"] == 0


def test_a_score_at_or_under_its_ceiling_is_not_reported(tmp_path):
    _, problems, _ = build(session(tmp_path, s1=0))
    assert not any(p.startswith("judge-ceiling") for p in problems)


def test_no_guidance_rule_set_by_the_chair_gives_s1_a_ceiling_of_two(tmp_path):
    dash, _, _ = build(session(tmp_path, s1=3), no_guidance="numeric")
    s1 = dash["decision"]["scores"][0]
    assert s1["ceiling"] == 2 and s1["final"] == 2


def test_planted_failure_judge_raises_the_position_above_the_rule(tmp_path):
    dash, _, _ = build(session(tmp_path, s1=0, position="Buy"))
    d = dash["decision"]
    assert d["position"]["key"] == "wait" and "rule's position stands" in d["position"]["judge_note"]


def test_planted_failure_reader_line_says_buy_when_the_position_is_wait(tmp_path):
    _, problems, _ = build(session(tmp_path, s1=0, not_own="Buy"))
    assert any("reader line says Buy" in p for p in problems)


def test_planted_failure_storyline_not_ten_lines_is_reported(tmp_path):
    _, problems, _ = build(session(tmp_path, s1=0, story="1. only one line (case book s3)."))
    assert any("storyline has 1 lines, not 10" in p for p in problems)


def test_a_standing_hard_gate_makes_the_position_avoid(tmp_path):
    dash, _, _ = build(session(tmp_path, s1=0, position="Avoid"), gates={"G-C"})
    assert dash["decision"]["position"]["key"] == "avoid"


def test_the_final_turn_is_not_shown_as_a_hearing_panel(tmp_path):
    dash, _, _ = build(session(tmp_path))
    assert all(not t["id"].lower().startswith("judge final") for p in dash["hearing"] for t in p["turns"])


def test_write_all_makes_the_three_files_and_the_page_carries_the_data(tmp_path):
    dest = session(tmp_path, s1=0)
    dash, problems, case = build(dest)
    rep.write_all(dest, dash, problems, case)
    for name in ("dashboard.json", "report.md", "report.html"):
        assert (dest / name).exists()
    page = (dest / "report.html").read_text(encoding="utf-8")
    assert rep.MARKER not in page and '"company": "BIOCON"' in page
    assert "</script><script>" not in page.split('id="dash">')[1].split("</script>")[0]
    assert json.loads((dest / "dashboard.json").read_text(encoding="utf-8"))["decision"]["position"]["label"] == "Wait"
    assert "simulation" in page.lower() and "SEBI-registered" in page


def test_a_hearing_with_no_final_turn_stops_with_a_clear_message(tmp_path):
    dest = tmp_path / "sess"
    shutil.copytree(EXAMPLE, dest)
    try:
        rep.build(dest, gates=set(), price_on_file=True, results_on_file=True, no_guidance=None)
    except SystemExit as e:
        assert "Judge final" in str(e)
    else:
        raise AssertionError("expected a stop")
