#!/usr/bin/env python3
"""Cards for the last stages of the SOIC-lawyer hearing: cross-examination, closings, the judge's final.

    python stage_cards.py <session> cross <issueA> <issueB>      # X1..X4 and XA1..XA4 cards
    python stage_cards.py <session> closing                      # convict closing, lawyer closing
    python stage_cards.py <session> final                        # judge final, with the question-id map

The judge final needs an id for each lawyer question: the decisive question keeps the case book's id for its section, and each
further question gets Q<section>.9<k>, so the code ceiling can still be worked out. This script adds those ids to case.json's
`analyst_questions` (the list the code treats as the allowed ids) the first time it runs.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_cards import BASE_REF, HEAD, NO_BRAIN, ROOT, SOIC_REF  # noqa: E402

AGENTS = ROOT / ".claude" / "agents"
SOIC, BIOCON, JUDGE = AGENTS / "council-soic.md", AGENTS / "council-biocon.md", AGENTS / "court-judge.md"


def write(session: Path, name: str, text: str) -> Path:
    card = session / "work" / "cards" / name
    card.parent.mkdir(parents=True, exist_ok=True)
    card.write_text(text + "\n", encoding="utf-8")
    return card


def turn(session: Path, key: str, seq: str, heading: str) -> Path:
    return session / "work" / "turns" / f"{key}__{seq}__{heading}.md"


def lawyer_questions(session: Path, key: str) -> int:
    """How many real questions the lawyer asked on an issue (a REST turn is not a question)."""
    n = 0
    for f in (session / "work" / "turns").glob(f"{key}__*__Q* Lawyer.md"):
        if not f.read_text(encoding="utf-8").lstrip().upper().startswith("REST"):
            n += 1
    return n


def cross(session: Path, a: str, b: str) -> list:
    case = json.loads((session / "case.json").read_text(encoding="utf-8"))
    iss = {i["id"]: i for i in case["issues"]}
    out = []
    for first, key, base in ((1, a, 1), (3, b, 5)):
        files = ", ".join(iss[f"I{int(key[1:])}"]["convict_files"])
        for k in (0, 1):
            xq, xa = first + k, first + k
            seq = base + 2 * k
            q_out, a_out = turn(session, "cross", f"{seq:02d}", f"X{xq} Lawyer"), turn(session, "cross", f"{seq + 1:02d}", f"XA{xa} Convict")
            q = (HEAD.format(agent=SOIC, out=q_out) + f"\n\nThen follow the template \"Lawyer cross\" in {BASE_REF} (read it), as the SOIC seat and with your own method: name in WHY I ASK the SOIC check (a source id from your brain) that the contradiction or gap breaks. {NO_BRAIN}\n"
                 f"Values: repo root {ROOT}; session {session}; this is cross-examination question X{xq}, on the weak issue {key}. Read {session}/case-book.md and the whole of {session}/hearing.md"
                 + (f" (the convict's answer XA{xa - 1} to your last cross question is in it)." if k else ".")
                 + " Every number of three digits or more you write must be printed in the case book or the hearing; write a figure only as it is printed there.")
            ans = (HEAD.format(agent=BIOCON, out=a_out) + f"\n\nThen do the \"Convict answer (A1, A2, A3, WA1, WA2)\" template in {BASE_REF}. Values: repo root {ROOT}; session {session}; cross-examination answer XA{xa}; convict files (at most three): {files}. "
                   f"Read the Cross section of {session}/hearing.md for the question. Every figure of three digits or more carries its own date within 80 characters, every time it appears.")
            out += [write(session, f"cross__X{xq}_lawyer.md", q), write(session, f"cross__XA{xa}_convict.md", ans)]
    return out


def closing(session: Path) -> list:
    conv = (HEAD.format(agent=BIOCON, out=turn(session, "closing", "01", "Convict closing")) + f"\n\nThen follow the prompt headed \"ROAST ROOM COURTROOM, CLOSING: THE CONVICT\" in {BASE_REF}. Values: repo root {ROOT}; session {session}. Read your brain's _hot.md and the whole of {session}/hearing.md. Under 150 words, first person as the seat. Every figure of three digits or more carries its own date.")
    law = (HEAD.format(agent=SOIC, out=turn(session, "closing", "02", "Lawyer closing")) + f"\n\nThen follow the prompt headed \"ROAST ROOM COURTROOM, CLOSING: THE LAWYER\" in {BASE_REF}, as the SOIC seat. {NO_BRAIN}\nValues: repo root {ROOT}; session {session}. Read the whole of {session}/hearing.md and {session}/case-book.md. Under 150 words. Also name, in one sentence, which SOIC check (a source id from your brain) gave you the most useful question, and which gave the least. Every number of three digits or more must be printed in the case book or the hearing.")
    return [write(session, "closing__convict.md", conv), write(session, "closing__lawyer.md", law)]


def id_map(session: Path) -> list:
    case = json.loads((session / "case.json").read_text(encoding="utf-8"))
    rows = []
    for iss in case["issues"]:
        if not iss.get("section"):
            continue
        key = f"I{int(iss['id'][1:]):02d}"
        n = lawyer_questions(session, key)
        sec = int(re.match(r"Q(\d+)\.", iss["decisive"]).group(1))
        ids = [iss["decisive"]] + [f"Q{sec}.9{k}" for k in range(1, n)]
        for qid in ids:
            if qid not in iss["analyst_questions"]:
                iss["analyst_questions"].append(qid)
        rows.append(f"- {iss['id']} {iss['name']} (section {iss['section']}): hearing Q1 = {ids[0]} (decisive), " + ", ".join(f"Q{k + 1} = {ids[k]}" for k in range(1, len(ids))) + f" ({len(ids)} questions asked)")
    (session / "case.json").write_text(json.dumps(case, indent=1), encoding="utf-8")
    return rows


def final(session: Path) -> Path:
    rows = "\n".join(id_map(session))
    text = (HEAD.format(agent=JUDGE, out=turn(session, "final", "01", "Judge final")) + f"\n\nThen follow the prompt headed \"ROAST ROOM COURTROOM, JUDGE: THE FINAL\" in {BASE_REF} (section \"Judge final\"; read all of it, including the list of headings and line shapes you must keep). Values: repo root {ROOT}; session {session}. "
            f"Read {session}/case-book.md, the whole of {session}/hearing.md, {session}/notebook.md and {session}/external.md. Do NOT read any brain.\n\n"
            "From the Chair: gates standing: none. Current price on file: yes (week ending 2026-10-23). Latest results on file: yes (quarter ended 2026-06-30). The data pack gate line: " + json.loads((session / "case.json").read_text())["gate"] + ". The S1 no-guidance case: numeric (as the Chair set it in the first BIOCON hearing; the record is the same: a stated no-guidance policy plus dated numeric segment anchors).\n\n"
            "IMPORTANT, the lawyer in this hearing is the SOIC seat and it asked its own questions, 2 to 5 per issue. In SECTION SCORES, list states under these question ids (use exactly these ids, each once, one state each, taken from the judge note and close of that issue; the first question of each issue is the decisive one):\n" + rows + "\n"
            "Issues I1 and I2 have no section: use them only in DIRECTION and DIRECTION WHY. S1 draws on both I3 and I10. If a section has no id above, write `none`.\n"
            "In STORYLINE and every why-chain, end each line with an evidence id or `not in the record`. In WHY THE DEFENCE HELD OR DID NOT, add one plain sentence on how the SOIC lawyer's own method (risks first, forensic gates, value chain) shaped what was found, naming turn ids.")
    return write(session, "final__judge.md", text)


if __name__ == "__main__":
    s, what = Path(sys.argv[1]).resolve(), sys.argv[2]
    if what == "cross":
        print("\n".join(str(c) for c in cross(s, sys.argv[3], sys.argv[4])))
    elif what == "closing":
        print("\n".join(str(c) for c in closing(s)))
    else:
        print(final(s))
