#!/usr/bin/env python3
"""Pull a subagent's final report out of its task output file and write it as a hearing turn.

    python extract_handback.py <task-output-file> <out.md> "A1 Convict"

The task file is a JSONL transcript. The report is the `message` of the last SubagentHandback
call. The text is written under a `### <heading>` line, with the five convict labels made
plain (`**ANSWER**` alone on a line becomes `ANSWER: <next line>`), so the hearing guard reads it
the same way as a hand-copied turn.
"""
import json
import re
import sys
from pathlib import Path

ONE_LINE = ("ANSWER", "MOVE", "STATE I CLAIM")
LABELS = ONE_LINE + ("EVIDENCE", "WHAT WOULD SETTLE IT")


def last_handback(path: Path) -> str:
    report = None
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            blocks = json.loads(line).get("message", {}).get("content")
        except json.JSONDecodeError:
            continue
        for b in blocks if isinstance(blocks, list) else []:
            if b.get("type") == "tool_use" and b.get("name") == "SubagentHandback":
                report = b["input"]["message"]
    if report is None:
        raise SystemExit(f"no SubagentHandback report in {path}")
    return report


def plain_labels(text: str) -> str:
    lines = [l.rstrip() for l in text.strip().splitlines()]
    out, i = [], 0
    while i < len(lines):
        m = re.fullmatch(r"\**(%s)\**:?\**" % "|".join(LABELS), lines[i].strip())
        if m:
            label = m.group(1)
            nxt = i + 1
            while label in ONE_LINE and nxt < len(lines) and not lines[nxt].strip():
                nxt += 1
            if label in ONE_LINE and nxt < len(lines):
                out.append(f"{label}: {lines[nxt].strip()}")
                i = nxt + 1
            else:
                out.append(f"{label}:")
                i += 1
        else:
            out.append(re.sub(r"^\**(%s)\**:\s*" % "|".join(LABELS), r"\1: ", lines[i]))
            i += 1
    return "\n".join(out)


def main() -> int:
    src, dest, heading = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(f"### {heading}\n\n{plain_labels(last_handback(src))}\n", encoding="utf-8")
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
