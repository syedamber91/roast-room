#!/usr/bin/env python3
"""Write a company seat's shareholding file from the filed shareholding patterns (made by soic-ladder's case_study_shareholding.py).

Every number is a value the company filed in its shareholding-pattern XBRL; the derived columns (change in promoter shares, implied
total shares, change in implied total shares) are computed here and labelled as derived. Nothing is estimated.
"""
import argparse
import csv
import hashlib
from datetime import datetime
from pathlib import Path


def parse(row):
    return datetime.strptime(row["period"], "%d-%b-%Y")


def render(rows: list, source_id: str, csv_sha: str, note: str) -> str:
    rows = sorted(rows, key=parse)
    out = [f"# Shareholding pattern, BIOCON: {source_id}", "",
           f"Generated from the shareholding-pattern filings on NSE (csv sha256 {csv_sha}); do not edit by hand. {len(rows)} filings, "
           f"{rows[0]['period']} to {rows[-1]['period']}. Percentages, share counts and encumbrance flags are as filed. {note}", "",
           "**How to cite.** (S0xx, shareholding filing for the quarter ended DD-MON-YYYY). A filing dated mid-quarter is an event-driven pattern, "
           "not a quarter end. The pledge columns are the company's own flags: `false` means the filing says no promoter shares are pledged.", "",
           "## Filed patterns", "",
           "| Period | Promoter shares | Promoter % | Public % | Employee trust % | Implied total shares (derived) | Pledged flag | Pledged or encumbered shares | Non-disposal undertaking flag | Other encumbrance flag | Filed |",
           "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        shares = f"{int(r['promoter_shares']):,}" if r["promoter_shares"] else ""
        total = f"{int(float(r['implied_total_shares'])):,}" if r["implied_total_shares"] else ""
        out.append(f"| {r['period']} | {shares} | {r['promoter_pct']} | {r['public_pct']} | {r['employee_trust_pct']} | {total} | {r['pledged']} | "
                   f"{r['pledged_or_encumbered_shares']} | {r['non_disposal_undertaking']} | {r['other_encumbrance']} | {r['broadcast'][:11]} |")
    first, last = rows[0], rows[-1]
    with_shares = [r for r in rows if r["promoter_shares"]]
    out += ["", "## Derived by code", ""]
    if len(with_shares) >= 2:
        a, b = with_shares[0], with_shares[-1]
        out.append(f"- Promoter shares {int(a['promoter_shares']):,} ({a['period']}) to {int(b['promoter_shares']):,} ({b['period']}): "
                   f"{int(b['promoter_shares']) - int(a['promoter_shares']):+,} shares. Promoter percentage {a['promoter_pct']} to {b['promoter_pct']}.")
        ta, tb = a.get("implied_total_shares"), b.get("implied_total_shares")
        if ta and tb:
            moved = int(b["promoter_shares"]) - int(a["promoter_shares"])
            out.append(f"- Implied total shares {int(float(ta)):,} to {int(float(tb)):,} ({100 * (float(tb) / float(ta) - 1):+.1f}%). The promoter's percentage "
                       f"fell while its own count moved by only {moved:+,} shares, so the fall comes from a larger total, not from promoter sales "
                       "(derived; the filings do not state the reason).")
    flags = {r["pledged"] for r in rows if r["pledged"]}
    out.append(f"- Pledged flag across the {len([r for r in rows if r['pledged']])} filings that carry one: {sorted(flags) or 'none carried'}.")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--csv", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--source-id", required=True)
    ap.add_argument("--note", default="")
    args = ap.parse_args()
    with open(args.csv, newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    args.out.write_text(render(rows, args.source_id, hashlib.sha256(args.csv.read_bytes()).hexdigest()[:12], args.note), encoding="utf-8")
    print(f"{len(rows)} filings written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
