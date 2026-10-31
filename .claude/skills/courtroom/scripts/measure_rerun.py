#!/usr/bin/env python3
"""Extract the re-run convict turns of one or more issues and compare guard notes before and after.

    python measure_rerun.py <session> <issue> [<issue> ...]

Reads work/rerun-map.json ({issue: {turn: task-id}}), takes each report from the task output
folder named by TASKS_DIR, writes work/rerun-<issue>/<turn>.md, then runs check_hearing on the
original convict answers of the same turns and on the re-runs and prints the counts by guard.
A turn whose task has no report yet is listed as pending and skipped on both sides.
"""
import collections
import importlib.util
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BRAIN = ROOT / ".claude" / "skills" / "roast-room" / "brains"


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def original_turns(session: Path, issue: str) -> dict:
    """{turn id: text} of the convict answers (A1-A3, WA1, WA2) as recorded in the hearing."""
    texts = {}
    for name in (f"{issue}-full.md", f"{issue}.md"):
        p = session / "work" / name
        if p.exists():
            texts.update({m.group(1): m.group(0) for m in re.finditer(r"(?ms)^### ((?:W?A)\d) Convict\n.*?(?=^### |\Z)", p.read_text(encoding="utf-8"))})
    for p in (session / "work").glob(f"W*-{issue}.md"):
        t = p.read_text(encoding="utf-8")
        m = re.match(r"### (WA\d) Convict", t)
        if m:
            texts[m.group(1)] = t
    return texts


def main() -> int:
    session, issues = Path(sys.argv[1]), sys.argv[2:]
    tasks_dir = Path(os.environ["TASKS_DIR"])
    eh, chk = load("extract_handback"), load("check_hearing")
    mapping = json.loads((session / "work" / "rerun-map.json").read_text(encoding="utf-8"))
    case_book = (session / "case-book.md").read_text(encoding="utf-8")
    external = (session / "external.md").read_text(encoding="utf-8")
    brains = BRAIN / "biocon-management", BRAIN / "india-market-analyst"
    for issue in issues:
        old, new, pending = [], [], []
        orig = original_turns(session, issue)
        for turn, task in mapping[issue].items():
            src = tasks_dir / f"{task}.output"
            try:
                text = f"### {turn} Convict\n\n{eh.plain_labels(eh.last_handback(src))}\n"
            except (SystemExit, FileNotFoundError):
                pending.append(turn)
                continue
            (session / "work" / f"rerun-{issue}").mkdir(exist_ok=True)
            (session / "work" / f"rerun-{issue}" / f"{turn}.md").write_text(text, encoding="utf-8")
            new.append(text)
            old.append(orig[turn])
        for label, turns in (("original", old), ("rerun", new)):
            body = f"## {issue} X\n\n" + "\n".join(turns)
            problems = chk.check(body, case_book, *brains, external)
            print(f"{issue} {label}: {len(problems)} notes {dict(collections.Counter(p.guard for p in problems))}")
        print(f"{issue} pending: {pending or 'none'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
