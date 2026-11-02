#!/usr/bin/env python3
"""Pull the facts a stakeholder page needs out of two finished hearings, with no model call.

    python stakeholder_data.py <analyst-session> <soic-session> <out.json>

For each hearing: the seven trust lamps, the judge's own red-flag lines, the triggers, and for every issue the lawyer's questions,
the convict's first-sentence answers (verbatim), the judge's state for each question and the first watch item. Nothing is rewritten.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_hearing as chk  # noqa: E402

STATE_WORDS = r"(answered|partial|no data|deflected|unverified)"


def first_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    m = re.match(r"(.+?[.!?])(?:\s|$)", text)
    return (m.group(1) if m else text)[:400]


def judge_states(body: str) -> dict:
    """{1: state, 2: state, ...} in the order the judge lists its question lines (a line starts with Q1, Q1.1 or Q10.2 style ids)."""
    m = re.search(r"STATE PROPOSED:?\s*\n?(.*?)(?=\n[A-Z][A-Z ]{5,}:|\Z)", body, re.S)
    out = {}
    for line in re.split(r"\s*//\s*|\n", m.group(1) if m else ""):
        line = line.strip().lstrip("-* ").strip()
        if not re.match(r"Q\d+(\.\d+)?\b", line):
            continue
        s = re.search(r"\b" + STATE_WORDS + r"\b", line)
        if s:
            out[len(out) + 1] = s.group(1)
    return out


def watch_first(body: str) -> str:
    m = re.search(r"WATCH:?\s*\n?(.*?)(?=\n[A-Z][A-Z ]{5,}:|\Z)", body, re.S)
    if not m:
        return ""
    line = next((l for l in m.group(1).splitlines() if l.strip()), "")
    return re.sub(r"^[-*\d.\s]+", "", line).strip()[:300]


def read(session: Path, who: str) -> dict:
    hearing = (session / "hearing.md").read_text(encoding="utf-8")
    turns = chk.parse_turns(hearing)
    dash = json.loads((session / "dashboard.json").read_text(encoding="utf-8"))["decision"]
    final = next(t["body"] for t in turns if t["id"] == "Judge final")
    flags = []
    m = re.search(r"RED FLAGS:\s*\n(.*?)\nPOSITION", final, re.S)
    for line in (m.group(1) if m else "").splitlines():
        parts = [p.strip() for p in line.lstrip("- ").split("|")]
        if len(parts) >= 3:
            flags.append({"qid": parts[0], "flag": parts[1], "evidence": parts[2]})
    issues = {}
    for t in turns:
        mi = re.match(r"(I\d+) (.*)", t["section"])
        if not mi:
            continue
        iid = mi.group(1)
        rec = issues.setdefault(iid, {"name": mi.group(2), "qa": {}, "states": {}, "watch": ""})
        f = chk.fields(t["body"])
        qn = re.match(r"Q(\d) Lawyer", t["id"])
        an = re.match(r"A(\d) Convict", t["id"])
        if qn:
            rec["qa"].setdefault(int(qn.group(1)), {})["question"] = f.get("QUESTION", "")
        elif an:
            rec["qa"].setdefault(int(an.group(1)), {})["answer"] = first_sentence(f.get("ANSWER", ""))
            rec["qa"][int(an.group(1))]["answer_turn"] = t["id"].split()[0]
        elif t["id"] in ("Judge note", "Judge close"):
            rec["states"].update(judge_states(t["body"]))
            if t["id"] == "Judge close":
                rec["watch"] = watch_first(t["body"]) or rec["watch"]
    for rec in issues.values():
        for n, qa in rec["qa"].items():
            qa["state"] = rec["states"].get(n, "")
    return {"who": who, "lamps": [{"section": r["section"], "name": r["name"], "judge": r["judge"], "ceiling": r["ceiling"], "final": r["final"], "cut": r["cut"]} for r in dash["scores"]],
            "total": dash["total"], "position": dash["position"]["label"], "direction": dash["direction"], "red_flags": flags,
            "triggers": dash["triggers"], "issues": issues}


if __name__ == "__main__":
    a, s, out = (Path(x) for x in sys.argv[1:4])
    Path(out).write_text(json.dumps({"analyst": read(a, "Analyst"), "soic": read(s, "SOIC")}, indent=1), encoding="utf-8")
    print("wrote", out)
