import importlib.util
from datetime import date
from pathlib import Path

spec = importlib.util.spec_from_file_location("bdp", Path(__file__).parent / "build_data_pack.py")
bdp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bdp)

NUMBERS = """# numbers

## Filed quarters

| Quarter | Revenue | Operating profit | Operating margin % |
|---|---|---|---|
| q1 | 100 | 10 | 10.0 |
| q2 | 110 | 11 | 10.0 |
| q3 | 120 | 12 | 10.0 |
| q4 | 130 | 13 | 10.0 |
| q5 | 120 | 24 | 25.0 |

## Next
text
"""

LINE = {"id": "D1", "label": "quarters", "required": True, "file": "numbers.md", "heading": "## Filed quarters", "kind": "table",
        "as_of": "2026-06-30", "max_age_days": 100,
        "derive": [{"name": "Growth", "op": "pct_change", "col": "Revenue", "lag": 4},
                   {"name": "Margin", "op": "ratio_pct", "num": "Operating profit", "den": "Revenue", "check_against": "Operating margin %"}]}


def brain(tmp_path):
    (tmp_path / "numbers.md").write_text(NUMBERS, encoding="utf-8")
    return tmp_path


def test_table_is_read_and_figures_are_derived_and_checked_by_code(tmp_path):
    line = bdp.build_line(LINE, brain(tmp_path), date(2026, 7, 30))
    assert line["state"] == "ok" and len(line["content"]) == 6
    assert any("Growth: 20.0%" in d for d in line["derived"])
    assert any("DISAGREES" in d and "q5: stated 25.0, computed 20.0" in d for d in line["derived"])


def test_old_line_is_stale_and_a_line_with_no_source_is_missing(tmp_path):
    stale = bdp.build_line(LINE, brain(tmp_path), date(2026, 12, 1))
    assert stale["state"] == "stale" and "limit 100" in stale["gap"]
    missing = bdp.build_line({"id": "D2", "label": "Q and A", "required": True, "file": None, "gap": "none held"}, tmp_path, date(2026, 7, 30))
    assert missing["state"] == "missing" and missing["gap"] == "none held"
    absent = bdp.build_line({**LINE, "heading": "## No such section"}, tmp_path, date(2026, 7, 30))
    assert absent["state"] == "missing" and "no section" in absent["gap"]


def test_gate_reads_incomplete_with_the_ids_and_complete_when_nothing_is_missing(tmp_path):
    brain(tmp_path)
    spec = {"company": "X", "brain": str(tmp_path), "lines": [LINE, {"id": "D2", "label": "Q and A", "required": True, "file": None}]}
    pack = bdp.build_pack(spec, tmp_path, date(2026, 7, 30))
    assert "**BRIEF INCOMPLETE: missing D2**" in pack and "Nobody fills a hole" in pack
    ok = bdp.build_pack({"company": "X", "brain": str(tmp_path), "lines": [LINE]}, tmp_path, date(2026, 7, 30))
    assert "**BRIEF COMPLETE**" in ok


def test_a_web_sourced_required_line_makes_the_brief_incomplete(tmp_path):
    brain(tmp_path)
    web = {**LINE, "id": "D3", "web_source": "a news page"}
    pack = bdp.build_pack({"company": "X", "brain": str(tmp_path), "lines": [web]}, tmp_path, date(2026, 7, 30))
    assert "unverified D3" in pack and "web source (a news page)" in pack


def test_pack_replaces_its_own_block_in_the_brief_and_keeps_the_rest(tmp_path):
    session = tmp_path / "s"
    session.mkdir()
    (session / "brief.md").write_text("# Brief\nthe decision\n", encoding="utf-8")
    bdp.write_into_brief(session, f"{bdp.START}\nfirst\n{bdp.END}")
    bdp.write_into_brief(session, f"{bdp.START}\nsecond\n{bdp.END}")
    text = (session / "brief.md").read_text(encoding="utf-8")
    assert "second" in text and "first" not in text and "the decision" in text and text.count(bdp.START) == 1


def test_a_partial_line_is_named_in_the_gate(tmp_path):
    brain(tmp_path)
    part = {**LINE, "id": "D5", "partial": "annual report only"}
    pack = bdp.build_pack({"company": "X", "brain": str(tmp_path), "lines": [part]}, tmp_path, date(2026, 7, 30))
    assert "partial D5" in pack and "Partial: annual report only" in pack
