#!/usr/bin/env python3
"""Join the per-turn files of a session into hearing.md.

    python assemble_hearing.py sessions/<session>

Turn files are <session>/work/turns/<key>__<seq>__<heading>.md. Keys in hearing order: opening, I01..I10, cross, closing.
The body of each file goes under a `### <heading>` line; each key gets a `## ` section line (an issue's comes from case.json).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_handback import plain_labels  # noqa: E402

KEYS = ["opening"] + [f"I{n:02d}" for n in range(1, 11)] + ["cross", "closing", "final"]
TITLES = {"opening": "Opening", "cross": "Cross", "closing": "Closing", "final": "Judge final"}


def section_title(key: str, case: dict) -> str:
    if key in TITLES:
        return TITLES[key]
    issue = next(i for i in case["issues"] if i["id"] == f"I{int(key[1:])}")
    return f"{issue['id']} {issue['name']}"


def assemble(session: Path) -> str:
    case = json.loads((session / "case.json").read_text(encoding="utf-8"))
    files = {}
    for f in (session / "work" / "turns").glob("*__*__*.md"):
        key, seq, heading = f.stem.split("__", 2)
        files.setdefault(key, []).append((seq, heading, f))
    out = [f"# Hearing: {case['company']}, SOIC analyst as lawyer\n"]
    for key in KEYS:
        if key not in files:
            continue
        out.append(f"\n## {section_title(key, case)}\n")
        for _seq, heading, f in sorted(files[key]):
            body = f.read_text(encoding="utf-8")
            if heading.endswith(" Lawyer") and body.lstrip().upper().startswith("REST"):
                heading = "Lawyer rest"    # the lawyer chose to stop: not a question, so no question shape is checked
            out.append(f"### {heading}\n{plain_labels(body)}\n")
    return "\n".join(out)


if __name__ == "__main__":
    s = Path(sys.argv[1])
    (s / "hearing.md").write_text(assemble(s), encoding="utf-8")
    print("wrote", s / "hearing.md")
