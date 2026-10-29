#!/usr/bin/env python3
"""Write a company seat's statement file from a verified annual-report statement record.

The record is the tiers csv made in soic-ladder (scripts/annual_report_prose.py verify). This script copies each kept statement
(tier High or Medium) verbatim into one generated brain file, grouped by type, with its page, section and speaker, so the
seat can quote it with a source id and Grep it by type heading. It never edits a quote.

  python build_statement_file.py --csv docs/company-record/biocon/tiers-prose-FY26-v2.csv \
    --out .claude/skills/roast-room/brains/biocon-management/statements-ar-fy26.md \
    --source-id S027 --company BIOCON --fy FY26 --year-end 2026-03-31
"""
import argparse
import csv
import hashlib
from pathlib import Path

TYPES = {
    "T01": "Management outlook and guidance", "T02": "Management explanation of results, one-offs and exceptional items",
    "T03": "Debt, leverage, refinancing and rating", "T04": "Capex, capacity and R&D",
    "T05": "Accounting policy and estimate changes, restatements", "T06": "Risks the company names and mitigations",
    "T07": "Auditor opinion, key audit matters, emphasis of matter", "T08": "Auditor name, tenure, fees, rotation",
    "T09": "CARO remarks and internal financial control opinion", "T10": "Board composition, independence, attendance, departures",
    "T11": "Promoter statements: holding, pledge, succession", "T12": "Related party policy, approvals, material transactions",
    "T13": "Subsidiaries and minority holders, stake changes", "T14": "Litigation, regulatory inspections, tax orders, penalties",
    "T15": "Subsequent events and going concern",
}
SECTION_LABEL = {
    "letter": "message from the chairperson or chief executive (management speech)",
    "mgmt_discussion": "management discussion and analysis (management speech)",
    "directors_report": "Board's report (company filing)",
    "governance": "corporate governance report (company filing)",
    "auditor_report": "independent auditor's report (the auditor's words)",
    "notes": "notes to the financial statements (company filing)",
}
KEPT = ("High", "Medium")
DEFAULT_VERIFICATION = ("Two verification cycles did not meet their bars (27 of 30 and 26 of 30 sampled statements marked right); "
                        "the owner accepted the record on 2026-10-29 with that limit.")


def read_rows(path: Path) -> list:
    with open(path, newline="", encoding="utf-8-sig") as handle:
        return [r for r in csv.DictReader(handle) if r["tier"] in KEPT]


def clean(text: str) -> str:
    """One line, nothing else changed (a quote must stay verbatim; line breaks inside a cell become spaces)."""
    return " ".join(text.split())


def render(rows: list, source_id: str, company: str, fy: str, year_end: str, csv_sha: str, verification: str = "", note: str = "") -> str:
    high = sum(r["tier"] == "High" for r in rows)
    out = [f"# Statements from the {company} annual report {fy}: {source_id}", "",
           f"Generated from the verified statement record (csv sha256 {csv_sha}); do not edit by hand. Year ended {year_end}. "
           f"{len(rows)} statements: {high} High, {len(rows) - high} Medium.", "",
           "**What a tier means.** High: the words are on the cited page in two independent text readers and in the part of the report "
           "the type belongs to. Medium (marked one reader): on the page in one reader only, mostly table rows. A tier says the words "
           "are on the page. It does not say the statement is true, complete or representative. " + (verification or DEFAULT_VERIFICATION), "",
           ] + ([f"**Known attribution limits.** {note}", ""] if note else []) + [
           f"**How to cite.** Quote verbatim with the source id, the page and the part of the report: (S{source_id[1:]}, p213, Board's report). "
           "The chairperson's and chief executive's messages and the management discussion are management speech. The auditor's report is "
           "the auditor's words, not management's. The Board's report, the governance report and the notes are the company's filings. "
           "A table row is a filed cell run, not something anyone said. Never present any of it as spoken by a person it did not come from.", "",
           "**What is missing.** Types the code does not take from a part of the report, a few table rows the checker refused, pages no "
           "extraction read, and every statement in the sustainability report. The tables of the same report are in numbers.md (S026).", ""]
    for code, label in TYPES.items():
        group = sorted((r for r in rows if r["type"] == code), key=lambda r: (int(r["page"]), r["claim_id"]))
        out += [f"## {code} {label}", "", f"{len(group)} statements." if group else "No statement kept for this type.", ""]
        for r in group:
            flag = "" if r["tier"] == "High" else " (one reader)"
            where = SECTION_LABEL.get(r["section"], r["section"])
            out.append(f'- p{r["page"]}{flag}: "{clean(r["quote"])}" ({source_id}, p{r["page"]}, {where})')
        out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--source-id", required=True)
    ap.add_argument("--company", required=True)
    ap.add_argument("--fy", required=True)
    ap.add_argument("--year-end", required=True)
    ap.add_argument("--verification", default="", help="what was checked for this year and how it scored")
    ap.add_argument("--note", default="", help="known attribution limits for this year")
    args = ap.parse_args()
    rows = read_rows(args.csv)
    args.out.write_text(render(rows, args.source_id, args.company, args.fy, args.year_end,
                               hashlib.sha256(args.csv.read_bytes()).hexdigest()[:12], args.verification, args.note), encoding="utf-8")
    print(f"{len(rows)} statements written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
