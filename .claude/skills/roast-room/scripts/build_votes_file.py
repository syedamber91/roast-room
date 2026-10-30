#!/usr/bin/env python3
"""Write a company seat's shareholder-vote file from the voting results the company filed (made by soic-ladder's case_study_votes.py).

Every number is a vote count or percentage as printed in the Regulation 44(3) annex; the grouping and the two thresholds used to pick out
resolutions are applied here, by code, and stated in the file. Nothing is estimated. A promoter group that is interested in a resolution does
not vote on it, so on those resolutions "votes against" is the public's alone; the file says so and shows the promoters' votes polled.
"""
import argparse
import csv
import hashlib
import re
from collections import defaultdict
from pathlib import Path

TOTAL_AGAINST_FLAG = 5.0      # percent of all votes polled
INSTITUTIONS_AGAINST_FLAG = 10.0  # percent of the public institutions' votes polled


def is_rpt(row) -> bool:
    return bool(re.search(r"related party", row["resolution"], re.I))


def short(text: str, n: int) -> str:
    text = text.replace("|", "/").replace("‐", "-").replace("‑", "-").strip(" -‐‑")
    return text if len(text) <= n else text[: n - 1].rstrip() + "..."


def render(rows: list, csv_sha: str) -> str:
    rows = sorted(rows, key=lambda r: (r["meeting_date"], int(r["resolution_no"])))
    f = lambda r, k: float(r[k]) if r[k] != "" else 0.0  # noqa: E731
    out = [f"# Shareholder votes, BIOCON: S034", "",
           f"Generated from the voting-results annexes Biocon filed with the exchanges (csv sha256 {csv_sha}); do not edit by hand. {len(rows)} resolutions at "
           f"{len({r['meeting_date'] for r in rows})} general meetings or postal ballots, {min(r['meeting_date'] for r in rows)} to {max(r['meeting_date'] for r in rows)}. "
           "Counts and percentages are as printed. S034 is voting numbers, not management speech, so no quote is taken from it.", "",
           "**How to cite.** (S034, voting results for the meeting dated DD-MON-YYYY, resolution N). The date is the meeting date, or for a postal ballot the date the results were filed.", "",
           "**What the percentages mean.** \"Against\" is the share of votes polled, not of shares. A promoter group that is interested in a resolution does not vote on it "
           "(its votes polled read 0 below), so on those resolutions the percentage against is the public's alone. The wording of a resolution is as printed in the annex and can be cut short there.", ""]
    out += ["## Related party resolutions by meeting", "",
            "| Meeting | Related party resolutions | Promoter group interested in | Highest % against (all votes) | Highest % against (public institutions) | The one with the highest % against |",
            "|---|---|---|---|---|---|"]
    by = defaultdict(list)
    for r in rows:
        if is_rpt(r):
            by[r["meeting_date"]].append(r)
    for date in sorted(by):
        rs = by[date]
        top = max(rs, key=lambda r: f(r, "total_against_pct"))
        out.append(f"| {date} | {len(rs)} | {sum(r['promoter_interested'] == 'Yes' for r in rs)} | {max(f(r, 'total_against_pct') for r in rs):.2f} | "
                   f"{max(f(r, 'institutions_against_pct') for r in rs):.2f} | resolution {top['resolution_no']}: {short(top['resolution'], 110)} |")
    out += ["", f"## Resolutions with {TOTAL_AGAINST_FLAG:g}% or more of all votes against, or {INSTITUTIONS_AGAINST_FLAG:g}% or more of the public institutions' votes against", "",
            "The two thresholds are this file's own, chosen to pick out resolutions where a visible block of votes went against; the course states none.", "",
            "| Meeting | No. | Type | Promoter group interested | % against (all) | % against (institutions) | % against (non-institutions) | Resolution (as printed) |",
            "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if f(r, "total_against_pct") >= TOTAL_AGAINST_FLAG or f(r, "institutions_against_pct") >= INSTITUTIONS_AGAINST_FLAG:
            out.append(f"| {r['meeting_date']} | {r['resolution_no']} | {r['type']} | {r['promoter_interested']} | {f(r, 'total_against_pct'):.2f} | "
                       f"{f(r, 'institutions_against_pct'):.2f} | {f(r, 'non_institutions_against_pct'):.2f} | {short(r['resolution'], 140)} |")
    out += ["", "## All resolutions", "",
            "| Meeting | No. | Type | Promoter group interested | Promoter votes polled | % against (all) | % against (institutions) | Votes against | Votes polled | Resolution (as printed) |",
            "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        out.append(f"| {r['meeting_date']} | {r['resolution_no']} | {r['type']} | {r['promoter_interested']} | {int(f(r, 'promoter_votes_polled')):,} | "
                   f"{f(r, 'total_against_pct'):.2f} | {f(r, 'institutions_against_pct'):.2f} | {int(f(r, 'total_against_votes')):,} | {int(f(r, 'total_votes_polled')):,} | {short(r['resolution'], 100)} |")
    bad = [r for r in rows if r["checks"] != "ok"]
    out += ["", "## Derived by code", "",
            f"- {len(rows)} resolutions read; {len(bad)} failed a check (the three holder categories add to the printed total for votes polled, for and against).",
            f"- {sum(is_rpt(r) for r in rows)} are related party resolutions; {sum(is_rpt(r) and r['promoter_interested'] == 'Yes' for r in rows)} of those had the promoter group interested.",
            f"- {sum(f(r, 'total_against_pct') >= TOTAL_AGAINST_FLAG for r in rows)} resolutions had {TOTAL_AGAINST_FLAG:g}% or more of all votes against; "
            f"{sum(f(r, 'institutions_against_pct') >= INSTITUTIONS_AGAINST_FLAG for r in rows)} had {INSTITUTIONS_AGAINST_FLAG:g}% or more of the public institutions' votes against."]
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--csv", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    with open(args.csv, newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    args.out.write_text(render(rows, hashlib.sha256(args.csv.read_bytes()).hexdigest()[:12]), encoding="utf-8")
    print(f"{len(rows)} resolutions written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
