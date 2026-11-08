#!/usr/bin/env python3
"""Write a company seat's quarterly results file from the filed results lines (made by soic-ladder's case_study_results.py).

Two inputs: the results XBRL (each quarter as filed, up to the quarter NSE's list reaches) and the results PDFs (three quarter columns per
filing). For each quarter after the XBRL ends, the row is ONE filing column: the column with the most cells read among those whose own
arithmetic ties, the latest filing winning a tie, with the filing and column named. A cell is never filled from another filing's column,
and a number is never repaired: a cell that was not read says "not read". Derived columns (year-on-year revenue growth, profit as a share of
revenue) are computed here and labelled. Money is Rs million as filed (consolidated), EPS per share.
"""
import argparse
import calendar
import csv
import hashlib
from datetime import date, datetime
from pathlib import Path

COLUMNS = ("this", "preceding", "year_ago")
KEYS = ("revenue_from_operations", "other_income", "income", "expenses", "finance_costs", "profit_before_tax", "tax_expense", "profit_for_period", "eps_basic")
HEAD = ("Revenue from operations", "Other income", "Total income", "Total expenses", "Finance costs", "Profit before tax", "Tax expense", "Profit for the period", "EPS basic")


def month_end(year: int, month: int) -> date:
    return date(year, month, calendar.monthrange(year, month)[1])


def quarter_of(filing_end: date, column: str) -> date:
    if column == "this":
        return filing_end
    if column == "year_ago":
        return month_end(filing_end.year - 1, filing_end.month)
    y, m = (filing_end.year, filing_end.month - 3) if filing_end.month > 3 else (filing_end.year - 1, filing_end.month + 9)
    return month_end(y, m)


def cells_read(row: dict) -> int:
    return sum(row.get(k, "") not in ("", None) for k in KEYS)


def pick_pdf_quarters(pdf_rows: list) -> dict:
    """quarter end -> the one filing column used: the most cells read among columns with no failed tie, the latest filing winning a tie."""
    best: dict = {}
    for r in pdf_rows:
        if r["problems"] or r["revenue_from_operations"] in ("", None):
            continue
        q = quarter_of(date.fromisoformat(r["period_end"]), r["column"])
        key = (cells_read(r), r["period_end"])
        if q not in best or key >= (cells_read(best[q]), best[q]["period_end"]):
            best[q] = r
    return best


def money(v) -> str:
    return "not read" if v in ("", None) else f"{float(v):,.0f}"


def eps(v) -> str:
    return "not read" if v in ("", None) else f"{float(v):.2f}"


def cells(row: dict) -> str:
    return " | ".join(eps(row.get(k)) if k == "eps_basic" else money(row.get(k)) for k in KEYS)


def render(xbrl_rows: list, pdf_rows: list, xbrl_sha: str, pdf_sha: str, xbrl_last: date, company: str = "BIOCON", source_id: str = "S044",
           company_name: str = None) -> str:
    company_name = company_name or company
    parse = lambda s: datetime.strptime(s, "%d-%b-%Y").date()  # noqa: E731
    out = [f"# Quarterly results, {company}: {source_id}", "",
           f"Generated from the consolidated quarterly results {company_name} filed (results XBRL, csv sha256 {xbrl_sha}; results PDFs, csv sha256 {pdf_sha}); do not edit by hand. "
           f"Rs million as filed, EPS per share. {source_id} is filed numbers, not management speech, so no quote is taken from it. Each row is one filing's own cells: "
           "nothing is estimated, repaired or filled from another filing, and a cell that was not read says so.", "",
           f"**How to cite.** ({source_id}, results filing for the quarter ended DD-MON-YYYY, column X).", "",
           "## Filed quarters", "",
           "| Quarter ended | " + " | ".join(HEAD) + " | Source |", "|---|" + "---|" * (len(HEAD) + 1)]
    table = {}
    notes = []
    for r in sorted(xbrl_rows, key=lambda r: parse(r["period_end"])):
        q = parse(r["period_end"])
        table[q] = r
        out.append(f"| {q.isoformat()} | {cells(r)} | own filing (XBRL, sha256 {r['xbrl_sha256']}) |")
        if r["problems"]:
            notes.append(f"- {q.isoformat()} (XBRL): {r['problems']}. The numbers are as filed.")
    chosen = pick_pdf_quarters(pdf_rows)
    quarters = sorted(q for q in chosen if q > xbrl_last)
    for q in quarters:
        r = chosen[q]
        table[q] = r
        which = "own filing" if r["column"] == "this" else f"printed in the filing for {r['period_end']} ({r['column'].replace('_', ' ')} column)"
        out.append(f"| {q.isoformat()} | {cells(r)} | {which}, {r['source_file']} |")
    covered = set(quarters)
    last = max(covered) if covered else xbrl_last
    missing = []
    q = xbrl_last
    while q < last:
        q = month_end(q.year + (q.month + 3 > 12), (q.month + 3 - 1) % 12 + 1)
        if q not in covered:
            missing.append(q.isoformat())
    bad = sorted({(r["period_end"], r["column"]) for r in pdf_rows if r["problems"] and r["column"] == "this"})
    out += ["", "## Not read", "",
            "- Quarters after the XBRL with no usable PDF column: " + (", ".join(missing) if missing else "none") + ". A column whose own lines do not add up, or whose "
            "revenue line was not read, is not used for a number; a damaged scan can leave single cells unread inside a row that is used.",
            "- Columns that failed their own arithmetic: " + ("; ".join(f"{p} ({c})" for p, c in bad) if bad else "none") + "."]
    if notes:
        out += ["", "## Notes from the filings' own checks", ""] + notes
    derived = []
    for q in sorted(table):
        prev = month_end(q.year - 1, q.month)
        row, old = table[q], table.get(prev)
        if old and row.get("revenue_from_operations") not in ("", None) and old.get("revenue_from_operations") not in ("", None) and float(old["revenue_from_operations"]) > 0:
            derived.append(f"{q.isoformat()}: revenue {100 * (float(row['revenue_from_operations']) / float(old['revenue_from_operations']) - 1):+.1f}% against {prev.isoformat()}")
        if row.get("revenue_from_operations") not in ("", None) and row.get("profit_for_period") not in ("", None) and float(row["revenue_from_operations"]) > 0:
            derived.append(f"{q.isoformat()}: profit is {100 * float(row['profit_for_period']) / float(row['revenue_from_operations']):.1f}% of revenue")
    out += ["", "## Derived by code", ""] + ([f"- {d}" for d in derived] or ["- none"])
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--xbrl-csv", required=True, type=Path)
    ap.add_argument("--pdf-csv", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--company", default="BIOCON")
    ap.add_argument("--source-id", default="S044")
    ap.add_argument("--company-name", default=None)
    args = ap.parse_args()
    read = lambda p: list(csv.DictReader(open(p, newline="", encoding="utf-8-sig")))  # noqa: E731
    xbrl, pdf = read(args.xbrl_csv), read(args.pdf_csv)
    xbrl_last = max(datetime.strptime(r["period_end"], "%d-%b-%Y").date() for r in xbrl)
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()[:12]  # noqa: E731
    args.out.write_text(render(xbrl, pdf, sha(args.xbrl_csv), sha(args.pdf_csv), xbrl_last, args.company, args.source_id, args.company_name), encoding="utf-8")
    print(f"{len(xbrl)} XBRL rows and {len(pdf)} PDF rows written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
