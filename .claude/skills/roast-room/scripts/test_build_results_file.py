import importlib.util
from datetime import date
from pathlib import Path

spec = importlib.util.spec_from_file_location("br", Path(__file__).parent / "build_results_file.py")
br = importlib.util.module_from_spec(spec)
spec.loader.exec_module(br)


def xrow(period, rev, pat, problems="", eps="2.5", other="10", inc=None, exp="50", pbt="30", tax="8", fin="1"):
    inc = inc if inc is not None else str(float(rev) + float(other))
    return {"period_end": period, "filed": "01-Jan-2025 10:00", "basis": "Consolidated", "revenue_from_operations": rev, "other_income": other, "income": inc,
            "expenses": exp, "finance_costs": fin, "profit_before_tax": pbt, "tax_expense": tax, "profit_for_period": pat, "eps_basic": eps,
            "problems": problems, "xbrl_url": "u", "xbrl_sha256": "abcd"}


def prow(period, column, rev, pat="", problems="", other="", inc="", exp="", pbt="", tax="", fin="", eps=""):
    return {"period_end": period, "column": column, "revenue_from_operations": rev, "other_income": other, "income": inc, "expenses": exp, "finance_costs": fin,
            "profit_before_tax": pbt, "tax_expense": tax, "profit_for_period": pat, "eps_basic": eps, "problems": problems, "source_file": f"f-{period}.pdf"}


def test_quarter_dates_for_the_three_columns():
    end = date(2026, 3, 31)
    assert br.quarter_of(end, "this") == end and br.quarter_of(end, "preceding") == date(2025, 12, 31) and br.quarter_of(end, "year_ago") == date(2025, 3, 31)


def test_a_quarter_after_the_xbrl_comes_from_the_filing_column_with_the_most_cells_that_tie_and_the_filing_is_named():
    pdf = [prow("2026-03-31", "this", "100"), prow("2026-03-31", "preceding", "90", pat="9", pbt="12", tax="3", inc="95", other="5"),
           prow("2026-06-30", "this", "110", pat="11", pbt="14", tax="3", inc="116", other="6"),
           prow("2026-06-30", "preceding", "100", pat="8", pbt="11", tax="3", inc="104", other="4")]
    chosen = br.pick_pdf_quarters(pdf)
    assert chosen[date(2026, 3, 31)]["profit_for_period"] == "8" and chosen[date(2026, 3, 31)]["period_end"] == "2026-06-30"  # preceding column of the Jun filing beats the 1-cell own column
    assert chosen[date(2025, 12, 31)]["profit_for_period"] == "9"
    assert chosen[date(2026, 6, 30)]["profit_for_period"] == "11"


def test_a_column_that_fails_its_own_ties_is_not_used_for_a_number():
    pdf = [prow("2026-06-30", "this", "110", pat="11", pbt="14", tax="3", inc="116", other="6", problems="profit before tax: printed 3,629 vs lines 2,578")]
    assert br.pick_pdf_quarters(pdf) == {}


def test_cells_are_never_filled_from_another_filings_column():
    pdf = [prow("2026-06-30", "this", "110", pat="", pbt="14", tax="3", inc="116", other="6"),
           prow("2026-09-30", "preceding", "110", pat="11", pbt="14", tax="3", inc="116", other="6")]
    chosen = br.pick_pdf_quarters(pdf)
    text = br.render([], pdf, "x", "y", date(2024, 12, 31), company="PIIND", source_id="S044")
    row = next(l for l in text.splitlines() if l.startswith("| 2026-06-30"))
    assert "11" in row  # the Sep 2026 filing's preceding column has the profit, so that column is chosen whole
    assert chosen[date(2026, 6, 30)]["profit_for_period"] == "11"


def test_the_table_has_a_title_a_source_column_and_says_not_read_for_a_blank_cell():
    xbrl = [xrow("30-Sep-2024", "100", "20")]
    pdf = [prow("2026-06-30", "this", "110", pat="", pbt="14", tax="3", inc="116", other="6", exp="100")]
    text = br.render(xbrl, pdf, "x", "y", date(2024, 9, 30), company="PIIND", source_id="S044")
    assert text.startswith("# Quarterly results, PIIND: S044") and "(S044, results filing" in text
    assert "| 2024-09-30 | 100 |" in text and "XBRL" in text
    assert "not read" in next(l for l in text.splitlines() if l.startswith("| 2026-06-30"))


def test_a_filings_own_flag_is_kept_in_the_notes_and_the_numbers_are_not_repaired():
    xbrl = [xrow("30-Jun-2024", "100", "20", problems="owners' share tag (profit to owners plus minority): filed 4,544 vs lines 4,488")]
    text = br.render(xbrl, [], "x", "y", date(2024, 6, 30), company="PIIND", source_id="S044")
    assert "owners' share tag" in text and "| 2024-06-30 | 100 |" in text


def test_derived_growth_and_margin_are_computed_by_code_and_labelled():
    xbrl = [xrow("30-Jun-2023", "100", "10"), xrow("30-Sep-2023", "110", "11"), xrow("31-Dec-2023", "120", "12"), xrow("31-Mar-2024", "130", "13"),
            xrow("30-Jun-2024", "125", "25")]
    text = br.render(xbrl, [], "x", "y", date(2024, 6, 30), company="PIIND", source_id="S044")
    assert "Derived by code" in text and "2024-06-30: revenue +25.0% against 2023-06-30" in text and "profit is 20.0% of revenue" in text
