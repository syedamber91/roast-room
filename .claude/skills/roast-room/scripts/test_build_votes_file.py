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


def test_the_company_and_source_id_are_parameters_and_default_to_biocon():
    rows = [row("2025-08-08", "1", "Adopt accounts", "0.01", "0.0")]
    assert bv.render(rows, "abc").startswith("# Shareholder votes, BIOCON: S034")
    text = bv.render(rows, "abc", source_id="S042", company="PIIND", company_name="PI Industries")
    assert text.startswith("# Shareholder votes, PIIND: S042") and "PI Industries filed" in text and "(S042, voting results" in text


def test_when_no_wording_was_read_the_related_party_count_is_not_available_not_zero():
    rows = [row("2025-08-08", "6", "", "17.96", "5"), row("2025-08-08", "7", "", "10.67", "5")]
    text = bv.render(rows, "abc", source_id="S042", company="PIIND", company_name="PI Industries")
    assert "wording was not read" in text and "related party count is not available" in text
    assert "0 are related party resolutions" not in text


def test_a_resolution_whose_numbers_could_not_be_read_is_shown_as_not_read_not_as_zero_votes():
    bad = row("2023-08-17", "1", "", "", "")
    bad["checks"] = "UNREADABLE: 0 total lines, 0 not readable, expected 4"
    for k in ("promoter_votes_polled", "total_against_pct", "institutions_against_pct", "total_against_votes", "total_votes_polled"):
        bad[k] = ""
    good = row("2025-08-14", "1", "Adopt accounts", "0.03", "0.07")
    good["checks"] = "ok"
    text = bv.render([bad, good], "abc", source_id="S042", company="PIIND", company_name="PI Industries")
    line = next(l for l in text.splitlines() if l.startswith("| 2023-08-17 | 1 |"))
    assert "not read" in line and "| 0 |" not in line


def test_a_stray_wording_on_a_few_rows_does_not_turn_an_unknown_related_party_count_into_zero():
    rows = [row("2025-08-08", "1", "stray header text", "1", "1")] + [row("2025-08-08", str(i), "", "1", "1") for i in range(2, 8)]
    text = bv.render(rows, "abc", source_id="S042", company="PIIND", company_name="PI Industries")
    assert "related party count is not available" in text
