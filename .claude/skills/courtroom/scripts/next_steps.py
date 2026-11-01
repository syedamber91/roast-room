#!/usr/bin/env python3
"""Say what each issue needs next, write the task cards for it, and remember what was already handed out.

    python next_steps.py <session> [--mark]

Per issue, from the turn files present:
  Qn Lawyer -> An Convict -> Q(n+1) ... until a lawyer file starts with REST (or Q5 is answered)
  -> Lawyer review (Opus) -> Judge note (Opus) -> WA1 and WA2 Convict (together) -> Judge close (Opus).
Prints one line per card: `<model> <card path>`. With --mark, a card is written to work/ledger.txt so the next run does not hand it out again.
A card whose turn file is missing but which is in the ledger is "in flight" and is skipped. Delete a ledger line to redo a turn.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_cards import build  # noqa: E402

MAX_Q = 5
OPUS = {"review", "judge_note", "judge_close"}


def files_of(session: Path, key: str) -> dict:
    return {f.stem.split("__", 2)[2]: f for f in (session / "work" / "turns").glob(f"{key}__*__*.md")}


def steps_for(session: Path, key: str) -> list:
    have = files_of(session, key)
    if "Judge close" in have:
        return []
    if "Judge note" in have:
        out = [("convict_a", w) for w in ("WA1", "WA2") if f"{w} Convict" not in have]
        return out or [("judge_close", "")]
    if "Lawyer review" in have:
        return [("judge_note", "")]
    for n in range(1, MAX_Q + 1):
        q = have.get(f"Q{n} Lawyer")
        if q is None:
            return [("lawyer_q", str(n))]
        if q.read_text(encoding="utf-8").lstrip().upper().startswith("REST"):
            return [("review", "")]
        if f"A{n} Convict" not in have:
            return [("convict_a", f"A{n}")]
    return [("review", "")]


def main(argv: list) -> None:
    session = Path(argv[0]).resolve()
    ledger = session / "work" / "ledger.txt"
    done = set(ledger.read_text().split("\n")) if ledger.exists() else set()
    handed = []
    for k in [f"I{n:02d}" for n in range(1, 11)]:
        for kind, arg in steps_for(session, k):
            card, _out = build(session, kind, k, arg)
            if card.name in done:
                continue
            print(("opus  " if kind in OPUS else "sonnet"), card)
            handed.append(card.name)
    if "--mark" in argv and handed:
        with open(ledger, "a") as f:
            f.write("\n".join(handed) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
