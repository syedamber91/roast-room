import importlib.util
from datetime import date
from pathlib import Path

spec = importlib.util.spec_from_file_location("bg", Path(__file__).parent / "build_segments_file.py")
bg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bg)


def pdf(period, section, segment, a, b, c, check="yes"):
    return {"filing_period_end": period, "section": section, "segment": segment, "this_quarter": a, "preceding_quarter": b, "year_ago_quarter": c, "segments_add_to_total": check}


def table(period, check="yes"):
    return [pdf(period, "revenue", "Biosimilars", 10.0, 9.0, 8.0, check), pdf(period, "revenue", "(total)", 10.0, 9.0, 8.0, check),
            pdf(period, "result", "Biosimilars", 1.0, 2.0, 3.0, check), pdf(period, "result", "(total)", 1.0, 2.0, 3.0, check)]


def test_quarter_dates_for_the_three_columns():
    end = date(2026, 3, 31)
    assert bg.quarter_of(end, "this_quarter") == end and bg.quarter_of(end, "preceding_quarter") == date(2025, 12, 31)
    assert bg.quarter_of(end, "year_ago_quarter") == date(2025, 3, 31) and bg.quarter_of(date(2026, 6, 30), "preceding_quarter") == date(2026, 3, 31)


def test_the_latest_filing_that_adds_up_supplies_a_quarter_and_a_filing_that_does_not_is_never_used():
    rows = table("2026-03-31") + table("2026-06-30") + table("2026-12-31", check="NO: this_quarter: x")
    chosen = bg.pick_quarters(rows)
    assert chosen[date(2026, 3, 31)] == ("2026-06-30", "preceding_quarter") and chosen[date(2026, 6, 30)] == ("2026-06-30", "this_quarter")
    assert date(2026, 12, 31) not in chosen
