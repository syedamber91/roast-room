import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("bv", Path(__file__).parent / "build_votes_file.py")
bv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bv)


def row(date, no, text, total, inst, interested="No", polled="5"):
    return {"meeting_date": date, "resolution_no": no, "type": "Ordinary", "resolution": text, "promoter_interested": interested, "promoter_votes_polled": polled,
            "institutions_against_pct": inst, "non_institutions_against_pct": "0.1", "total_against_pct": total, "total_against_votes": "10", "total_votes_polled": "1000", "checks": "ok"}


def test_related_party_items_are_grouped_by_meeting_and_the_flagged_table_uses_the_two_thresholds():
    rows = [row("2025-08-08", "6", "To approve material related party transactions between A and B", "0.94", "0.94", "Yes", "0"),
            row("2025-08-08", "16", "To approve increase in the limits", "6.83", "20.83"),
            row("2025-08-08", "1", "Adopt accounts", "0.01", "0.0"),
            row("2026-06-08", "5", "Appoint a director", "2.0", "10.5")]
    text = bv.render(rows, "abc")
    assert "| 2025-08-08 | 1 | 1 | 0.94 | 0.94 |" in text
    flagged = text.split("## Resolutions with")[1].split("## All resolutions")[0]
    assert "increase in the limits" in flagged and "Appoint a director" in flagged and "Adopt accounts" not in flagged
    assert "4 resolutions read; 0 failed a check" in text
