import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("bs", Path(__file__).parent / "build_shareholding_file.py")
bs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bs)


def row(period, shares, pct, total, pledged="false"):
    return {"period": period, "broadcast": "01-JAN-2026 10:00", "promoter_shares": str(shares), "promoter_pct": pct, "public_pct": "1", "employee_trust_pct": "0",
            "implied_total_shares": str(total), "pledged": pledged, "pledged_or_encumbered_shares": "", "non_disposal_undertaking": "", "other_encumbrance": ""}


def test_rows_are_sorted_by_date_and_the_derived_lines_come_from_the_first_and_last_filing():
    text = bs.render([row("31-MAR-2026", 100, "50", 200), row("30-SEP-2021", 99, "99", 100)], "S032", "abc", "")
    assert text.index("30-SEP-2021") < text.index("31-MAR-2026") and "## Filed patterns" in text
    assert "+1 shares" in text and "(+100.0%)" in text and "not from promoter sales" in text and "['false']" in text
