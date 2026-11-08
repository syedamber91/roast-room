import json
import importlib.util
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("lite_court", HERE / "lite_court.py")
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)

ANS = """+ env something
Q: What was revenue in Q1?
  ANSWER: 17,023 Rs million  (deck deck-q1fy27 p5)
Q: What was borrowings 2026?
  ANSWER: 2,383 Rs million  (annual-report AR p242)
Q: What was the ratio?
  REFUSE: the model found no answer in the excerpts
Q: What FIFA World Cup winner year was mentioned?
  REFUSE: the model found no answer in the excerpts
"""
MAP = {"control": [4], "issues": {
    "I3": {"questions": [1], "decisive": 1},
    "I6": {"questions": [2, 3], "decisive": 2},
    "I9": {"questions": [], "decisive": None}}}
ISSUES = {"I3": {"name": "Guidance", "section": "S1"}, "I6": {"name": "Debt", "section": "S4"},
          "I9": {"name": "Board", "section": "S7"}}


def test_parse_sets_state_by_code():
    rows = lc.parse_answers(ANS, MAP["control"])
    assert [r["state"] for r in rows] == ["answered", "answered", "refused", "control"]
    assert rows[0]["figure"] == "17,023 Rs million" and rows[0]["source"] == "deck deck-q1fy27" and rows[0]["cite"] == "p5"
    assert rows[2]["reason"].startswith("the model found no answer")


def test_answered_control_stops_the_run():
    bad = ANS.replace("Q: What FIFA World Cup winner year was mentioned?\n  REFUSE: the model found no answer in the excerpts",
                      "Q: What FIFA World Cup winner year was mentioned?\n  ANSWER: 2022  (annual-report AR p1)")
    with pytest.raises(ValueError, match="control"):
        lc.parse_answers(bad, [4])


def test_control_never_counted():
    res = lc.run(ANS, MAP, ISSUES, lambda p: "")
    assert res["counts"] == {"asked": 3, "answered": 2, "refused": 1, "control_refused": 1}


def test_issue_with_no_question_is_no_data_and_ceiling_zero():
    res = lc.run(ANS, MAP, ISSUES, lambda p: "")
    assert res["issues"]["I9"]["state"] == "no data"
    s7 = next(r for r in res["sections"] if r["section"] == "S7")
    assert s7["ceiling"] == 0 and s7["final"] == 0


def test_ceiling_from_code_and_refused_is_no_data():
    res = lc.run(ANS, MAP, ISSUES, lambda p: "")
    s4 = next(r for r in res["sections"] if r["section"] == "S4")
    assert s4["ceiling"] == 2          # decisive answered, one other refused
    assert res["issues"]["I6"]["questions"][3]["state"] == "no data"


GOOD = 'NOTE: Revenue is stated with a page.\nQUOTE: "17,023 Rs million"\nSCORE: 3\n'


def test_judge_can_only_lower():
    res = lc.run(ANS, MAP, ISSUES, lambda p: 'NOTE: n\nQUOTE: "2,383 Rs million"\nSCORE: 3\n')
    s4 = next(r for r in res["sections"] if r["section"] == "S4")
    assert s4["judge"] == 3 and s4["final"] == 2 and s4["cut"]
    res = lc.run(ANS, MAP, ISSUES, lambda p: 'NOTE: n\nQUOTE: "17,023 Rs million"\nSCORE: 0\n')
    s1 = next(r for r in res["sections"] if r["section"] == "S1")
    assert s1["ceiling"] == 3 and s1["final"] == 0


def test_quote_verified_in_answers():
    res = lc.run(ANS, MAP, ISSUES, lambda p: GOOD)
    assert res["issues"]["I3"]["notes"][0]["quote"] == "17,023 Rs million"


def test_bad_quote_rewritten_once_then_kept_only_if_it_passes():
    calls = []

    def gen(p):
        calls.append(p)
        if "NOT FOUND" in p:
            return GOOD
        return 'NOTE: invented\nQUOTE: "99,999 Rs million"\nSCORE: 3\n'
    res = lc.run(ANS, MAP, ISSUES, gen)
    notes = res["issues"]["I3"]["notes"]
    assert len(notes) == 1 and notes[0]["quote"] == "17,023 Rs million"
    assert any("NOT FOUND" in c for c in calls)


def test_bad_quote_twice_is_dropped_never_kept():
    res = lc.run(ANS, MAP, ISSUES, lambda p: 'NOTE: invented\nQUOTE: "99,999 Rs million"\nSCORE: 3\n')
    assert res["issues"]["I3"]["notes"] == []
    assert res["issues"]["I3"]["dropped"] == 1


def test_judge_not_called_for_no_data_issue():
    seen = []
    lc.run(ANS, MAP, ISSUES, lambda p: seen.append(p) or "")
    assert not any("I9" in p.splitlines()[0] for p in seen)


def test_position_never_buy_without_price_and_gates_not_checked():
    res = lc.run(ANS, MAP, ISSUES, lambda p: "")
    assert res["position_key"] in ("wait", "wait_good")
    assert res["position_key"] != "buy"


def test_report_says_not_comparable_first_and_gates_unchecked():
    res = lc.run(ANS, MAP, ISSUES, lambda p: GOOD)
    html = lc.render_report(res, "PI Industries (PIIND)")
    body = html.split("<body", 1)[1]
    assert body.index("not comparable") < body.index("Trust")
    assert "Gates were not checked" in html


def test_receipts_list_question_figure_cite_status():
    res = lc.run(ANS, MAP, ISSUES, lambda p: "")
    html = lc.render_receipts(res, "PI Industries (PIIND)")
    for s in ("What was revenue in Q1?", "17,023 Rs million", "deck deck-q1fy27", "p5", "refused"):
        assert s in html
    assert html.count("What was revenue in Q1?") == 1


def test_real_issue_map_covers_each_question_once_and_not_the_control():
    m = json.loads((HERE.parent / "references" / "lite-issues.json").read_text())
    nums = [n for i in m["issues"].values() for n in i["questions"]]
    assert sorted(nums) == [n for n in range(1, 51) if n != 49]
    for i in m["issues"].values():
        assert i["decisive"] is None or i["decisive"] in i["questions"]


def test_cli_offline_writes_both_pages(tmp_path, monkeypatch):
    monkeypatch.delenv("NVIDIA_API_KEY", raising=False)
    f = tmp_path / "a.md"
    f.write_text(ANS)
    mp = tmp_path / "m.json"
    mp.write_text(json.dumps(MAP))
    code = lc.main(["--answers", str(f), "--out", str(tmp_path / "o"), "--map", str(mp), "--judge", "none"])
    assert code == 0
    assert (tmp_path / "o" / "lite-report.html").exists() and (tmp_path / "o" / "lite-receipts.html").exists()


def test_reasons_do_not_claim_dates_or_print_none():
    res = lc.run(ANS, MAP, ISSUES, lambda p: "")
    why = " ".join(r["ceiling_why"] for r in res["sections"])
    assert "number and a date" not in why and "question none" not in why
    s1 = next(r for r in res["sections"] if r["section"] == "S1")
    assert "page cite" in s1["ceiling_why"]
    s7 = next(r for r in res["sections"] if r["section"] == "S7")
    assert "no data-point question" in s7["ceiling_why"]


def test_report_warns_answered_is_not_clean():
    res = lc.run(ANS, MAP, ISSUES, lambda p: "")
    assert "Answered does not mean good" in lc.render_report(res, "X")


def test_quote_may_copy_figure_with_its_cite_as_written_in_the_answers_file():
    rows = lc.parse_answers(ANS, [4])
    assert lc.quote_ok("17,023 Rs million  (deck deck-q1fy27 p5)", rows)
    assert lc.quote_ok("17,023 Rs million (deck deck-q1fy27 p5)", rows)
    assert not lc.quote_ok("17,023 Rs million (deck deck-q1fy27 p6)", rows)


def test_rejected_quotes_and_raw_replies_are_kept_for_diagnosis():
    res = lc.run(ANS, MAP, ISSUES, lambda p: 'NOTE: x\nQUOTE: "99,999 Rs million"\nSCORE: 2\n')
    i3 = res["issues"]["I3"]
    assert i3["rejected"] == ["99,999 Rs million", "99,999 Rs million"]
    assert len(i3["raw"]) == 2 and "99,999" in i3["raw"][0]


def test_prompt_does_not_punish_missing_detail_and_asks_for_short_exact_quote():
    p = lc.judge_prompt("I6", "Debt", lc.parse_answers(ANS, [4]))
    assert "missing detail is not a reason" in p.lower()
    assert "copy" in p.lower() and "1 to 8 words" in p
    assert "contradict" in p.lower()
