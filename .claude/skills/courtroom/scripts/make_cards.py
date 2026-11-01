#!/usr/bin/env python3
"""Write one task card per hearing turn, so each agent prompt can be a single line: "Read <card> and do exactly what it says."

    python make_cards.py <session> lawyer_q I05 2          # lawyer question 2 of issue I5
    python make_cards.py <session> convict_a I05 A2        # convict answer A2 (also WA1, WA2, XA1..)
    python make_cards.py <session> review I05              # lawyer's issue review (Opus)
    python make_cards.py <session> judge_note I05          # judge note after the last answer
    python make_cards.py <session> judge_close I05         # judge close after the why answers

Cards live in <session>/work/cards/. The turn file the agent must write is named inside the card.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
REFS = ROOT / ".claude" / "skills" / "courtroom" / "references"
SOIC_REF = REFS / "hearing-prompts-soic-lawyer.md"
BASE_REF = REFS / "hearing-prompts.md"
NO_BRAIN = "HARD RULE: never open anything under /home/user/roast-room/.claude/skills/roast-room/brains/biocon-management/ or any other company brain; you learn the company only from case-book.md and the hearing. Put a quotation mark round text only if you copied it exactly from your own brain folder (checked with Grep first); otherwise paraphrase with no quotation marks."
HEAD = "Read {agent} and follow it as your instructions for this whole task. You may read files and write exactly one file: {out} . Write only the turn body (no ### heading). Do not write any other file. Reply with the word written."


def issue_of(case, key):
    return next(i for i in case["issues"] if i["id"] == f"I{int(key[1:])}")


def turn_path(session, key, seq, heading):
    return session / "work" / "turns" / f"{key}__{seq}__{heading}.md"


def build(session: Path, kind: str, key: str, arg: str = "") -> tuple:
    case = json.loads((session / "case.json").read_text(encoding="utf-8"))
    iss = issue_of(case, key)
    top = f"repo root {ROOT}; session {session}; issue {iss['id']} \"{iss['name']}\""
    gaps = "; ".join(iss["known_gaps"]) or "none listed"
    soic = ROOT / ".claude/agents/council-soic.md"
    biocon = ROOT / ".claude/agents/council-biocon.md"
    judge = ROOT / ".claude/agents/court-judge.md"
    if kind == "lawyer_q":
        n = int(arg)
        out = turn_path(session, key, f"{2 * n - 1:02d}", f"Q{n} Lawyer")
        text = (HEAD.format(agent=soic, out=out) + f"\n\nThen follow the template \"Lawyer question (Q1 to Q5)\" in {SOIC_REF} (read the whole file first). {NO_BRAIN}\n"
                f"Values: {top}; QUESTION {n}. Known gaps: {gaps}. Data pack state: {iss['state']}. Read the {iss['id']} section of {session}/hearing.md first: the convict's last answer decides your ladder step. "
                f"If you are at Q3 or later and your method's checks are covered, you may write only REST: one line (see the template). At Q5 you must write REST. Write DECISIVE: no.")
    elif kind == "convict_a":
        seq = {"A1": "02", "A2": "04", "A3": "06", "A4": "08", "A5": "10", "WA1": "13", "WA2": "14"}[arg]
        n = arg[-1]
        out = turn_path(session, key, seq, f"{arg} Convict")
        files = ", ".join(iss["convict_files"])
        text = (HEAD.format(agent=biocon, out=out) + f"\n\nThen do the \"Convict answer (A1, A2, A3, WA1, WA2)\" template in {BASE_REF} (read it and the convict's answer shape in the same file). Values: {top}; turn {arg}; convict files (at most three): {files}. "
                f"Read the {iss['id']} section of {session}/hearing.md for the question. Answer the last lawyer question (or, for WA1/WA2, the judge's why question {n}) only.")
    elif kind == "review":
        out = turn_path(session, key, "11", "Lawyer review")
        text = (HEAD.format(agent=soic, out=out) + f"\n\nThen follow the template \"Lawyer issue review (Opus)\" in {SOIC_REF}. {NO_BRAIN}\nValues: {top}. Read {session}/case-book.md and the {iss['id']} section of {session}/hearing.md. "
                "EXTRA is allowed only if fewer than 5 questions were asked.")
    elif kind in ("judge_note", "judge_close"):
        close = kind == "judge_close"
        out = turn_path(session, key, "15" if close else "12", "Judge close" if close else "Judge note")
        section = "JUDGE: CLOSE ON" if close else "JUDGE: NOTE ON"
        text = (HEAD.format(agent=judge, out=out) + f"\n\nThen follow the prompt headed \"ROAST ROOM COURTROOM, {section} [issue id and name]\" in {BASE_REF} (section \"Judge {'close' if close else 'note'}\"). Values: {top}. "
                f"Read {session}/case-book.md, the {iss['id']} section of {session}/hearing.md (the lawyer here is the SOIC seat; its questions carry a source id and a DECISIVE flag, and its 'Lawyer review' turn is its own consolidation), and {session}/notebook.md. Do NOT read any brain. "
                "Question labels in STATE PROPOSED are the hearing's own: Q1 is the decisive question, then Q2 and so on. "
                "CHECKS FROM CODE (pasted by the Chair): code ran over every turn of this issue with 0 problems; every quotation in the convict's turns was found word for word in the convict's brain with its id, and every figure of three digits or more in the convict's answers has a date within 80 characters. Say 'verified by code' for those quotes. "
                "The lawyer's 'Lawyer review' turn is its own consolidation; any EXTRA question it proposed was not asked (cost cap), so list that gap as a watch item if it matters.")
    else:
        raise SystemExit("unknown kind " + kind)
    card = session / "work" / "cards" / f"{key}__{kind}__{arg or 'x'}.md"
    card.parent.mkdir(parents=True, exist_ok=True)
    card.write_text(text + "\n", encoding="utf-8")
    return card, out


if __name__ == "__main__":
    s = Path(sys.argv[1]).resolve()
    card, out = build(s, sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
    print(card)
