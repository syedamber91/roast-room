import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("bsf", Path(__file__).parent / "build_statement_file.py")
bsf = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bsf)

ROWS = [
    {"claim_id": "a", "page": "9", "section": "governance", "type": "T10", "quote": "Mr A\nattended 5 of 5 meetings", "tier": "High"},
    {"claim_id": "b", "page": "3", "section": "letter", "type": "T10", "quote": "We will reduce debt first", "tier": "Medium"},
    {"claim_id": "c", "page": "4", "section": "letter", "type": "T01", "quote": "dropped one", "tier": "Dropped"},
]


def test_only_kept_rows_are_written_with_page_flag_and_speaker():
    kept = [r for r in ROWS if r["tier"] in bsf.KEPT]
    text = bsf.render(kept, "S027", "BIOCON", "FY26", "2026-03-31", "abc")
    assert '- p3 (one reader): "We will reduce debt first" (S027, p3, message from the chairperson' in text
    assert '- p9: "Mr A attended 5 of 5 meetings" (S027, p9, corporate governance report (company filing))' in text
    assert "dropped one" not in text and "No statement kept for this type." in text


def test_quotes_are_in_page_order_within_a_type():
    kept = [r for r in ROWS if r["tier"] in bsf.KEPT]
    text = bsf.render(kept, "S027", "BIOCON", "FY26", "2026-03-31", "abc")
    assert text.index("p3 (one reader)") < text.index("- p9:")
