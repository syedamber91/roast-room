#!/usr/bin/env python3
"""Write a company seat's quarterly segment file from the filed segment tables (made by soic-ladder's case_study_segments*.py).

Two inputs: the results XBRL (each quarter as filed, up to the quarter NSE's list reaches) and the results PDFs (three quarter columns per
filing). For each quarter after the XBRL ends, the table shown is the one printed by the LATEST filing whose segments add to its own total
for both revenue and result, with the filing and column named on every row. Numbers are as printed, in Rs million; segment names are as
printed. Derived columns (a segment's result as a percentage of its revenue) are computed here and labelled. Nothing is estimated, and a
quarter with no clean source is listed as not read.
"""
import argparse
import calendar
import csv
import hashlib
from datetime import date
from pathlib import Path

COLUMNS = ("this_quarter", "preceding_quarter", "year_ago_quarter")


def month_end(year: int, month: int) -> date:
    return date(year, month, calendar.monthrange(year, month)[1])


def quarter_of(filing_end: date, column: str) -> date:
    if column == "this_quarter":
        return filing_end
    if column == "year_ago_quarter":
        return month_end(filing_end.year - 1, filing_end.month)
    y, m = (filing_end.year, filing_end.month - 3) if filing_end.month > 3 else (filing_end.year - 1, filing_end.month + 9)
    return month_end(y, m)


def pick_quarters(pdf_rows: list) -> dict:
    """quarter end -> (filing period end, column), the latest filing whose revenue and result tables both add up."""
    clean = {}
    for r in pdf_rows:
        clean.setdefault(r["filing_period_end"], set())
    for period in clean:
        mine = [r for r in pdf_rows if r["filing_period_end"] == period]
        if all(any(r["section"] == s and r["segments_add_to_total"] == "yes" for r in mine) for s in ("revenue", "result")):
            clean[period] = True
        else:
            clean[period] = False
    chosen = {}
    for period in sorted((p for p, ok in clean.items() if ok), reverse=False):
        end = date.fromisoformat(period)
        for column in COLUMNS:
            chosen[quarter_of(end, column)] = (period, column)  # a later filing overwrites an earlier one
    return chosen


def fmt(value) -> str:
    return "" if value in (None, "") else f"{float(value):,.0f}"


def render(xbrl_rows: list, pdf_rows: list, xbrl_sha: str, pdf_sha: str, xbrl_last: date) -> str:
    out = ["# Segments by quarter, BIOCON: S033", "",
           f"Generated from the segment tables Biocon filed (results XBRL, csv sha256 {xbrl_sha}; results PDFs, csv sha256 {pdf_sha}); do not edit by hand. "
           "Figures are Rs million, consolidated, as printed. Segment names are as printed. **The segments and the result measure changed over the period; "
           "read the Definitions section before comparing two quarters.** S033 is filed numbers, not management speech, so no quote is taken from it.", "",
           "**How to cite.** (S033, segment table in the filing for the quarter ended DD-MON-YYYY, column X).", ""]
    out += ["## Filed quarters, XBRL", "",
            "The result here is each segment's profit or loss BEFORE TAX AND FINANCE COSTS. Segments: Biosimilars, Generics, Novel Biologics, Research Services "
            "(Research services in some filings).", "",
            "| Quarter ended | Segment | Revenue | Result before tax and finance costs | Assets | Liabilities |", "|---|---|---|---|---|---|"]
    for r in xbrl_rows:
        out.append(f"| {r['period_end']} | {r['segment']} | {fmt(r['revenue_inr_m'])} | {fmt(r['result_before_tax_and_finance_cost_inr_m'])} | "
                   f"{fmt(r['assets_inr_m'])} | {fmt(r['liabilities_inr_m'])} |")
    chosen = pick_quarters(pdf_rows)
    quarters = sorted(q for q in chosen if q > xbrl_last)
    out += ["", "## Latest basis by quarter", "",
            "The result here is each segment's PROFIT BEFORE TAX from that segment, as the later filings print it (a different measure from the XBRL table above). "
            "Each quarter is read from the latest filing whose segment lines add to its own total for both revenue and result, and the filing and column are named.", "",
            "| Quarter ended | Segment (as printed) | Revenue | Result (profit before tax of the segment) | Printed in the filing for | Column |", "|---|---|---|---|---|---|"]
    derived = []
    for q in quarters:
        period, column = chosen[q]
        mine = [r for r in pdf_rows if r["filing_period_end"] == period and r["section"] in ("revenue", "result")]
        names = []
        for r in mine:
            if r["segment"] not in names:
                names.append(r["segment"])
        for name in names:
            rev = next((r[column] for r in mine if r["section"] == "revenue" and r["segment"] == name), "")
            res = next((r[column] for r in mine if r["section"] == "result" and r["segment"] == name), "")
            out.append(f"| {q.strftime('%d-%b-%Y').upper()} | {name} | {fmt(rev)} | {fmt(res)} | {period} | {column.replace('_', ' ')} |")
            if rev not in ("", None) and res not in ("", None) and float(rev) > 0 and not name.startswith("("):
                derived.append(f"{q.isoformat()} {name}: segment result is {100 * float(res) / float(rev):.1f}% of segment revenue")
    covered = set(quarters)
    wanted = [quarter_of(date.fromisoformat(max(r['filing_period_end'] for r in pdf_rows)), "this_quarter")]
    missing = []
    q = xbrl_last
    last = max(covered) if covered else xbrl_last
    while q < last:
        q = month_end(q.year + (q.month + 3 > 12), (q.month + 3 - 1) % 12 + 1)
        if q not in covered:
            missing.append(q.isoformat())
    out += ["", "## Not read", ""]
    out.append("- Quarters with no clean source in these filings: " + (", ".join(missing) if missing else "none") + ". "
               "A filing whose text layer is corrupted, or whose segment lines do not add to their own total, is not used for a number.")
    out += ["", "## Definitions that changed (from the filings' own notes)", "",
            "- Up to the XBRL period the segments are Biosimilars, Generics, Novel Biologics and Research Services, and the result is before tax and finance costs.",
            "- The later PDF tables show three segments: Biosimilars, Generics and Services (printed as CRDMO in the filings up to the quarter ended 2026-03-31), with the result as each segment's profit before tax.",
            "- The filing for the quarter ended 2026-03-31 moved the interest on optionally convertible debentures from Biosimilars to the unallocable line and restated earlier periods. "
            "The filing for the quarter ended 2026-06-30 moved cross charges of common utilities from Generics to the unallocable line and restated its comparatives.",
            "- So a quarter printed in a later filing can differ from the same quarter in an earlier one; the table above names the filing for each row.", "",
            "## Derived by code", ""]
    out += [f"- {d}" for d in derived] or ["- none"]
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--xbrl-csv", required=True, type=Path)
    ap.add_argument("--pdf-csv", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    read = lambda p: list(csv.DictReader(open(p, newline="", encoding="utf-8-sig")))  # noqa: E731
    xbrl, pdf = read(args.xbrl_csv), read(args.pdf_csv)
    for r in pdf:
        for c in COLUMNS:
            r[c] = float(r[c])
    from datetime import datetime
    ordered = sorted(xbrl, key=lambda r: datetime.strptime(r["period_end"], "%d-%b-%Y"))
    xbrl_last = max(datetime.strptime(r["period_end"], "%d-%b-%Y").date() for r in xbrl)
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()[:12]  # noqa: E731
    args.out.write_text(render(ordered, pdf, sha(args.xbrl_csv), sha(args.pdf_csv), xbrl_last), encoding="utf-8")
    print(f"{len(xbrl)} XBRL rows and {len(pdf)} PDF rows written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
