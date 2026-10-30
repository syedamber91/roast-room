import importlib.util
import json
import re
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
spec = importlib.util.spec_from_file_location("bcb", HERE / "build_case_book.py")
bcb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bcb)

SPEC = ROOT / "docs" / "company-record" / "biocon" / "datapack.json"
EVENTS = ROOT / "docs" / "company-record" / "biocon" / "announcements-2022-2026-2026-10-30.json"
QUESTIONS = ROOT / ".claude" / "skills" / "roast-room" / "brains" / "india-market-analyst" / "questions.md"


def real_build():
    return bcb.build("BIOCON", SPEC, EVENTS, date(2026, 10, 30))


def line(state="ok", partial=None, required=True, gap=""):
    return {"state": state, "partial": partial, "required": required, "gap": gap}


def test_the_issues_file_points_only_at_things_that_exist():
    config = json.loads(bcb.ISSUES_FILE.read_text(encoding="utf-8"))
    pack_ids = {l["id"] for l in json.loads(SPEC.read_text(encoding="utf-8"))["lines"]}
    analyst_ids = set(re.findall(r"^### (Q\d+\.\d+)", QUESTIONS.read_text(encoding="utf-8"), re.M))
    for issue in config["issues"]:
        assert set(issue["pack_lines"]) <= pack_ids, issue["id"]
        assert set(issue["analyst_questions"]) <= analyst_ids, issue["id"]
        assert issue["decisive"] in issue["analyst_questions"], issue["id"]
    baseline_ids = [b["id"] for b in config["baseline"]]
    assert len(baseline_ids) == len(set(baseline_ids)) == 26
    assert all(set(b["numbers_from"]) <= pack_ids for b in config["baseline"])
    assert [b["id"] for b in config["baseline"] if b["external"]] == ["B18", "B19", "B20", "B21", "B22"]


def test_issue_state_is_no_record_thin_or_examinable():
    lines = {"A": line(), "B": line(partial="p"), "C": line(state="missing", gap="none"), "D": line(state="stale", gap="old")}
    assert bcb.issue_state(["A", "B"], lines)[0] == "examinable"
    assert bcb.issue_state(["B"], lines)[0] == "thin"
    assert bcb.issue_state(["D"], lines)[0] == "thin"
    assert bcb.issue_state(["A", "C"], lines)[0] == "no record"
    assert bcb.issue_state(["A", "ZZ"], lines)[0] == "no record"      # a pack line the spec does not know is a hole, not a pass


def test_a_management_claim_line_is_dropped_but_a_job_title_and_a_filed_source_note_are_kept():
    bcb.DROPPED.clear()
    kept = bcb.strip_management_lines("- Management's 7% to 9% guidance was given\n- These are filed numbers, not management's words\n| a | b |", "3")
    assert "guidance" not in kept and "not management's words" in kept and "| a | b |" in kept
    assert len(bcb.DROPPED) == 1
    assert bcb.check_facts_only("| 2024-02-08 | Resignation | Resignation of Mr X as Senior Management Personnel |") == []
    assert bcb.check_facts_only("| row | guidance for FY27 |") != []                # a claim inside a table row fails loudly


def test_the_real_biocon_case_book_has_the_facts_chapters_and_marks_the_drafted_ones_not_yet_drafted():
    text, case = real_build()
    assert case["facts_only_problems"] == [] and case["gate"].startswith("BRIEF INCOMPLETE")
    quarters = re.findall(r"^\| (20\d\d-\d\d-\d\d) \| [\d,]+ \|", text.split("### Filed quarters")[1].split("### Full year")[0], re.M)
    assert len(quarters) == 11
    assert "| 2025-06-30 | 39,419 | 318 | 7,489 | 19.0 | 2,767 | 892 | 314 | +14.8 | +20.7 | +0.9 |" in text   # worked out by code from the filed cells
    assert "| 2026-06-30 | 43,360 | 442 | 8,472 | 19.5 | 2,132 | 1,368 | 1,411 | +10.0 | +13.1 | +0.5 |" in text
    assert "| 2023-12-31 | 39,537 | 4,050 | 9,268 | 23.4 | 2,667 | 7,533 | 6,600 | n/a | n/a | n/a |" in text          # no year-ago row: n/a, never a guess
    assert "Not yet drafted" in text and case["chapters"]["1"]["drafted"] is False and case["chapters"]["3"]["drafted"] is True
    states = {i["id"]: i["state"] for i in case["issues"]}
    assert states["I6"] == "examinable" and states["I10"] == "thin"
    assert "Subject with no recorded position in the convict's record: Share buybacks" in case["not_in_record"]
    assert case["dropped_management_lines"], "the brain's annual report notes quote management; the case book must say what it left out"


def test_the_timeline_comes_from_the_exchange_feed_with_the_exchanges_own_summary():
    text, case = real_build()
    timeline = text.split("## 6.")[1].split("## 7.")[0]
    assert "| Acquisition |" in timeline and "| Resignation |" in timeline and case["announcements_to"] >= "2026-10-01"
    assert len(re.findall(r"^\| 20\d\d-\d\d-\d\d \|", timeline, re.M)) > 20


def test_every_convict_file_hint_exists_in_the_biocon_brain_and_respects_the_three_file_rule():
    config = json.loads(bcb.ISSUES_FILE.read_text(encoding="utf-8"))
    brain = ROOT / ".claude" / "skills" / "roast-room" / "brains" / "biocon-management"
    groups = [i["convict_files"] for i in config["issues"]] + [b["convict_files"] for b in config["baseline_blocks"]]
    for files in groups:
        assert 1 <= len(files) <= 3 and all((brain / f).exists() for f in files), files
    blocks = {b["block"] for b in config["baseline"]}
    assert blocks == {name for group in config["baseline_blocks"] for name in group["baseline_blocks"]}   # every baseline question is in a block that a convict call covers
