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


def test_the_company_name_is_in_the_title_and_defaults_to_biocon():
    rows = [row("31-MAR-2026", 100, "50", 200), row("30-SEP-2021", 99, "99", 100)]
    assert bs.render(rows, "S032", "abc", "").startswith("# Shareholding pattern, BIOCON: S032")
    assert bs.render(rows, "S041", "abc", "", company="PIIND").startswith("# Shareholding pattern, PIIND: S041")


def test_a_real_fall_in_the_promoters_own_share_count_is_not_called_a_larger_total():
    # PIIND: 70,920,494 shares (46.74%) to 69,920,474 (46.09%): the promoter's own count fell by 1,000,020
    rows = [row("30-JUN-2022", 70920494, "46.74", 151718118), row("30-SEP-2022", 69920474, "46.09", 151718118)]
    text = bs.render(rows, "S041", "abc", "", company="PIIND")
    assert "not from promoter sales" not in text
    assert "-1,000,020 shares" in text and "own share count fell by 1,000,020" in text
