#!/usr/bin/env python3
"""Check the model-written parts of the stakeholder page against their sources. Code only, no model.

    python verify_plain.py <stakeholder-dir>

Reads flags-input.json, flags-merged.json, rows-input.json, rows-plain.json. Prints one line per problem; exit 1 if any.
Rules: every input flag appears once; a merged flag's text is copied exactly from a member; kid lines have no digits and respect word limits;
every figure of three digits or more (or with a comma) in a plain line appears in its source text; no buy, sell or hold words.
"""
import json
import re
import sys
from pathlib import Path

ADVICE = re.compile(r"\b(buy|sell|hold)\b", re.I)
FIG = re.compile(r"\d[\d,]*\.?\d*")


def figures(text: str) -> set:
    out = set()
    for m in FIG.findall(text):
        digits = m.rstrip(".,").replace(",", "")
        if len(digits.split(".")[0]) >= 3:
            out.add(digits)
    return out


def check_line(label: str, text: str, limit: int, kid: bool, source: str) -> list:
    out = []
    words = len(text.split())
    if words > limit:
        out.append(f"{label}: {words} words, limit {limit}")
    if kid and re.search(r"\d", text):
        out.append(f"{label}: kid line has a digit")
    if ADVICE.search(text):
        out.append(f"{label}: has a buy, sell or hold word")
    if not kid:
        extra = figures(text) - figures(source)
        if extra:
            out.append(f"{label}: figure(s) {sorted(extra)} not in the source")
    return out


def check_flags(inputs: list, merged: list) -> list:
    out, by_id, seen = [], {f["id"]: f for f in inputs}, []
    for m in merged:
        members = [by_id[i] for i in m["members"] if i in by_id]
        seen += m["members"]
        if len(members) != len(m["members"]):
            out.append(f"{m['id']}: unknown member id")
            continue
        if m["text"] not in [f["flag"] for f in members]:
            out.append(f"{m['id']}: text is not copied exactly from a member")
        sides = {f["who"] for f in members}
        want = "both" if sides == {"analyst", "soic"} else sides.pop()
        if m["found_by"] != want:
            out.append(f"{m['id']}: found_by is {m['found_by']}, members say {want}")
        source = " ".join(f["flag"] + " " + f["evidence"] for f in members)
        out += check_line(m["id"] + " kid", m["kid"], 12, True, source)
        out += check_line(m["id"] + " teen", m["teen"], 30, False, source)
    for fid in by_id:
        if seen.count(fid) != 1:
            out.append(f"{fid}: appears {seen.count(fid)} times in merged members, must be once")
    return out


def check_rows(inputs: list, plain: list) -> list:
    out, src = [], {r["key"]: r for r in inputs}
    got = {p["key"]: p for p in plain}
    for key in src:
        if key not in got:
            out.append(f"{key}: missing")
            continue
        s, p = src[key], got[key]
        text = " ".join([s["question"], s["answer"], s["watch"]])
        for field, limit, kid in (("kid_q", 14, True), ("teen_q", 25, False), ("kid_a", 14, True), ("teen_a", 30, False), ("kid_settle", 14, True), ("teen_settle", 25, False)):
            out += check_line(f"{key} {field}", p.get(field, ""), limit, kid, text)
    return out


def main(folder: Path) -> int:
    load = lambda n: json.loads((folder / n).read_text(encoding="utf-8"))
    problems = check_flags(load("flags-input.json"), load("flags-merged.json")) + check_rows(load("rows-input.json"), load("rows-plain.json"))
    for p in problems:
        print(p)
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1])))
