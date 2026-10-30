#!/usr/bin/env python3
"""Write a company seat's file of call questions that were not fully answered, from the checked Q&A state record.

Input is states.csv made in soic-ladder (scripts/case_study_qa_states.py): one row per item, each with the analyst's own words
(`asked`), a state and the management words that justify it (`evidence`), both checked by code to be verbatim passages of the call
transcript. Output is one generated brain file: a table of counts per call, then every item whose state is partial, deflected, declined
or deferred, grouped by call. Answered items are counted, not copied. Nothing is rewritten.

  python build_qa_states_file.py --csv docs/company-record/biocon/qa-states.csv --out <brain>/qa-states.md --calls "2022-11-15=S001,..."
"""
import argparse
import csv
import hashlib
from collections import Counter, defaultdict
from pathlib import Path

NOT_FULL = ("partial", "deflected", "declined", "deferred")
ORDER = ("answered",) + NOT_FULL + ("no answer turn", "unverified", "not judged")


def render(rows: list, calls: dict, csv_sha: str, check_note: str) -> str:
    by_call = defaultdict(list)
    for r in rows:
        by_call[r["held"]].append(r)
    out = ["# Call questions and how management answered them", "",
           f"Generated from the checked question-and-answer record (csv sha256 {csv_sha}); do not edit by hand. Each row is one thing an "
           "analyst asked. The analyst's words and management's words are both copied verbatim from the call transcript (code checked "
           "every passage), and the state is a model's reading of how well that answer met that question.", "",
           f"**What was checked.** {check_note}", "",
           "**How to cite.** The analyst's words are the analyst's, never management's: (S006, analyst question). Management's words: "
           "(S006, management answer). A state is a reading of one answer against one question. It does not say the answer was true, and "
           "a `deferred` that was answered on a later call is not tracked. Neighbouring states (answered or partial, partial or deflected) "
           "are the likeliest disagreements.", "",
           "## Counts per call", "",
           "| Call held | Source | " + " | ".join(ORDER) + " |", "|---|---|" + "---|" * len(ORDER)]
    for held in sorted(by_call):
        counts = Counter(r["state"] for r in by_call[held])
        out.append(f"| {held} | {calls[held]} | " + " | ".join(str(counts.get(s, 0)) for s in ORDER) + " |")
    total = Counter(r["state"] for r in rows)
    out += ["| all 14 calls | | " + " | ".join(str(total.get(s, 0)) for s in ORDER) + " |", "",
            "`no answer turn`: the pair has no management turn after the question (set by code). `not judged` and `unverified`: the model "
            "returned nothing usable for it; read the call.", ""]
    for held in sorted(by_call):
        items = [r for r in by_call[held] if r["state"] in NOT_FULL]
        sid = calls[held]
        out += [f"## {held} ({sid}): {len(items)} questions not fully answered", ""]
        for r in sorted(items, key=lambda r: int(r["pair"])):
            line = f'- {r["state"]} · pair {r["pair"]} · {r["analyst"]} asked: "{" ".join(r["asked"].split())}" ({sid}, analyst question)'
            if r["evidence"]:
                line += f' · management: "{" ".join(r["evidence"].split())}" ({sid}, management answer)'
            out.append(line)
        out.append("")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--calls", required=True, help="held=source id pairs, comma separated")
    ap.add_argument("--check-note", required=True)
    args = ap.parse_args()
    calls = dict(p.split("=") for p in args.calls.split(","))
    with open(args.csv, newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    args.out.write_text(render(rows, calls, hashlib.sha256(args.csv.read_bytes()).hexdigest()[:12], args.check_note), encoding="utf-8")
    print(f"{sum(r['state'] in NOT_FULL for r in rows)} not-fully-answered items of {len(rows)} rows written to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
