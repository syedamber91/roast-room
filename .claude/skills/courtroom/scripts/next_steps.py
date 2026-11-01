#!/usr/bin/env python3
"""Say what each issue needs next, and write the task cards for it.

    python next_steps.py <session>

Per issue, from the turn files present: Qn Lawyer -> An Convict -> Q(n+1) Lawyer ... until a lawyer file starts with REST (or Q5's answer is in),
then the lawyer review, then the judge note. Prints one line per issue: the card to run, or what is waiting.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_cards import build  # noqa: E402

MAX_Q = 5


def files_of(session: Path, key: str) -> dict:
    out = {}
    for f in (session / "work" / "turns").glob(f"{key}__*__*.md"):
        out[f.stem.split("__", 2)[2]] = f
    return out


def next_step(session: Path, key: str):
    have = files_of(session, key)
    if "Judge note" in have:
        return None, "judge note written; the judge's why questions (ASK NEXT) are handled by the Chair"
    if "Lawyer review" in have:
        return ("judge_note", ""), "review done"
    for n in range(1, MAX_Q + 1):
        q = have.get(f"Q{n} Lawyer")
        if q is None:
            return ("lawyer_q", str(n)), f"needs Q{n}"
        if q.read_text(encoding="utf-8").lstrip().upper().startswith("REST"):
            return ("review", ""), f"Q{n} is REST"
        if f"A{n} Convict" not in have:
            return ("convict_a", f"A{n}"), f"needs A{n}"
    return ("review", ""), "five questions answered"


if __name__ == "__main__":
    s = Path(sys.argv[1]).resolve()
    for k in [f"I{n:02d}" for n in range(1, 11)]:
        step, why = next_step(s, k)
        if step is None:
            print(k, "-", why)
            continue
        card, out = build(s, step[0], k, step[1])
        print(k, step[0], step[1], "->", card, "|", why, "| exists" if out.exists() else "")
