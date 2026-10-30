#!/usr/bin/env python3
"""Check a courtroom hearing for the honesty rules (docs/courtroom-design.md section 7). Code only, no model.

  python check_hearing.py sessions/<date>-court-<company>

Reads <session>/hearing.md, <session>/case-book.md, <session>/case.json (which names the convict's and the lawyer's brains) and, if it exists,
<session>/external.md. Prints one line per problem: `FAIL` problems make the exit code 1, `warn` problems do not.

The guards, by name:
  turn-shape     every turn has the fields its role needs, the convict uses at most two allowed moves, an allowed state, and the length limits hold
  quote-source   a convict quote is verbatim in the convict's brain and is followed by its id; a lawyer quote is verbatim in the lawyer's brain
                 or in an earlier turn; a judge quote is verbatim in the hearing or the case book (the judge never opens a brain)
  id-exists      every (S0nn) id a convict turn uses is in the convict brain's sources.md, every (Ennn) id is in external.md; no placeholder ids
  no-speech-id   an id whose source is filed numbers or a hand-read document (not management speech) never sits behind a quotation
  has-evidence   every convict answer carries an id or the words "not in my record"
  number-date    every number of three digits or more in a convict answer has a date, quarter or as-of word within 80 characters
  lawyer-number  every number of three digits or more in a lawyer turn is in the case book or an earlier turn
  external-id     an Ennn id is used only for an external point (baseline B18 to B22 or a line marked EXT)
  judge-story    every storyline line the judge writes ends in an evidence id or "not in the record"; "I did not understand" is never a bare "none"
  reading-level  (warning) a judge turn whose sentences average more than 25 words
Not here yet (step 5): a judge score above its code ceiling. Not here yet: the jargon-without-a-plain-definition check (needs the glossary).
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOM = Path(__file__).resolve().parents[2] / "roast-room"
BRAINS = ROOM / "brains"

MOVES = {"cite", "mitigate", "challenge", "concede", "not in my record"}
STATES = {"answered", "partial", "not in my record"}
NUMBER_DATE_WINDOW = 80   # characters either side of a number in which a date, quarter or as-of word must appear (tunable)
LIMITS = {"answer_words": 130, "evidence_lines": 8, "question_words": 70, "deflected_words": 70, "story_line_words": 40}
LABELS = ["ANSWER", "MOVE", "EVIDENCE", "STATE I CLAIM", "WHAT WOULD SETTLE IT", "EXT REQUEST", "TO", "QUESTION", "WHY I ASK", "IF DEFLECTED"]
LABEL_RE = re.compile(r"^(" + "|".join(LABELS) + r"):", re.M)
DATE_WORDS = re.compile(r"\d{4}-\d{2}-\d{2}|\b(?:19|20)\d{2}\b|\bFY ?'?\d{2,4}\b|\bQ[1-4]\b|\bas of\b|\bheld\b|\bquarter ended\b|\byear (?:to|ended)\b"
                        r"|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\b", re.I)
ID_RE = re.compile(r"\b(S\d{3}|E\d{3})\b")
PLACEHOLDER_RE = re.compile(r"\bS0xx\b|\bS\d{2}x\b|\bE0xx\b", re.I)
EVIDENCE_RE = re.compile(r"\(hearing|case book|\bS\d{3}\b|\bE\d{3}\b|not in the record|hearing I\d|\b(?:W?A|XA|Q|X)\d\b")


class Problem:
    def __init__(self, turn, guard, message, severity="FAIL"):
        self.turn, self.guard, self.message, self.severity = turn, guard, message, severity

    def __str__(self):
        return f"{self.severity:<4} {self.guard:<13} {self.turn}: {self.message}"


# ---- reading the hearing --------------------------------------------------------------------------------------------------------------

def norm(text: str) -> str:
    """The same quote matching the council uses: lower case, curly quotes made straight, punctuation to spaces, spaces squeezed."""
    text = text.lower().replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9' ]+", " ", text)).strip()


def parse_turns(hearing: str) -> list:
    """[{id, role, section, body}] for every '### ...' turn; the role is the word Lawyer, Convict or Judge in the heading."""
    turns, section = [], ""
    parts = re.split(r"^(#{2,3} .+)$", hearing, flags=re.M)
    for heading, body in zip(parts[1::2], parts[2::2]):
        if heading.startswith("## "):
            section = heading[3:].strip()
            continue
        title = heading[4:].strip()
        role = re.search(r"\b(Lawyer|Convict|Judge)\b", title)
        if role:
            turns.append({"id": title, "role": role.group(1), "section": section, "body": body.strip()})
    return turns


def fields(body: str) -> dict:
    """{LABEL: text} for the labelled fields of a turn (a label runs to the next label)."""
    found = list(LABEL_RE.finditer(body))
    out = {}
    for i, m in enumerate(found):
        end = found[i + 1].start() if i + 1 < len(found) else len(body)
        out[m.group(1)] = body[m.end():end].strip()
    return out


def words(text: str) -> int:
    return len(text.split())


def big_numbers(text: str) -> list:
    """[(digits, position)] for numbers of three digits or more, ignoring dates, years, source ids and page numbers."""
    masked = re.sub(r"\d{4}-\d{2}-\d{2}|\b(?:19|20)\d{2}\b|\b[SE]\d{3}\b|\bS0xx\b|PDF pages? \d+|\bp\d+\b|\bQ[1-4]\b|\bFY ?'?\d+\b", lambda m: " " * len(m.group()), text)
    found = []
    for m in re.finditer(r"(?<![\w.])\d{1,3}(?:,\d{3})+(?:\.\d+)?|(?<![\w.,])\d{3,}(?:\.\d+)?(?![\w])", masked):
        found.append((m.group().replace(",", ""), m.start()))
    return found


def quotes(text: str) -> list:
    """[(quote, following text)] for every quotation of five words or more."""
    out = []
    for m in re.finditer(r'"([^"\n]*)"', text):      # pair the quotation marks strictly left to right, so a short quote cannot shift the pairing
        if words(m.group(1)) >= 5:
            out.append((m.group(1), text[m.end():m.end() + 60]))
    return out


def sources_table(sources_text: str) -> dict:
    """{id: line} from a brain's sources.md ('- S026 | ... |')."""
    return {m.group(1): m.group(0) for m in re.finditer(r"^- ((?:S|E)\d{3}) \|.*$", sources_text, re.M)}


def non_speech_ids(table: dict) -> set:
    return {i for i, line in table.items() if "not management speech" in line or "no quote is taken" in line}


# ---- the guards -----------------------------------------------------------------------------------------------------------------------

def guard_turn_shape(turn) -> list:
    out, f, tid = [], fields(turn["body"]), turn["id"]
    if turn["role"] == "Convict" and re.match(r"^(A|WA|XA)\d+ ", tid):
        for need in ("ANSWER", "MOVE", "EVIDENCE", "STATE I CLAIM", "WHAT WOULD SETTLE IT"):
            if need not in f:
                out.append(Problem(tid, "turn-shape", f"missing {need}"))
        moves = [m.strip() for m in re.split(r"[;,]", re.sub(r"\(.*?\)", "", f.get("MOVE", ""))) if m.strip()]
        if len(moves) > 2 or any(m not in MOVES for m in moves):
            out.append(Problem(tid, "turn-shape", f"MOVE must be one or two of {sorted(MOVES)}, found {moves}"))
        state = re.split(r"[.:(]", f.get("STATE I CLAIM", ""))[0].strip().lower()
        if state not in STATES:
            out.append(Problem(tid, "turn-shape", f"STATE I CLAIM must be one of {sorted(STATES)}, found '{state}'"))
        if words(f.get("ANSWER", "")) > LIMITS["answer_words"]:
            out.append(Problem(tid, "turn-shape", f"ANSWER is {words(f['ANSWER'])} words, limit {LIMITS['answer_words']}"))
        lines = [l for l in f.get("EVIDENCE", "").splitlines() if l.strip().startswith("-")]
        if len(lines) > LIMITS["evidence_lines"]:
            out.append(Problem(tid, "turn-shape", f"EVIDENCE has {len(lines)} lines, limit {LIMITS['evidence_lines']}"))
    if turn["role"] == "Lawyer" and re.match(r"^(Q|X)\d+ ", tid):
        for need in ("TO", "QUESTION", "WHY I ASK", "IF DEFLECTED"):
            if need not in f:
                out.append(Problem(tid, "turn-shape", f"missing {need}"))
        if words(f.get("QUESTION", "")) > LIMITS["question_words"]:
            out.append(Problem(tid, "turn-shape", f"QUESTION is {words(f['QUESTION'])} words, limit {LIMITS['question_words']} (one ask, one number, one date)"))
        if words(f.get("IF DEFLECTED", "")) > LIMITS["deflected_words"]:
            out.append(Problem(tid, "turn-shape", f"IF DEFLECTED is {words(f['IF DEFLECTED'])} words, limit {LIMITS['deflected_words']} (one follow-up)"))
    return out


def guard_quotes(turn, earlier_text: str, case_book: str, convict_brain: str, lawyer_brain: str) -> list:
    out, tid = [], turn["id"]
    text = turn["body"]
    if turn["role"] == "Lawyer":    # the lawyer's own planned follow-up wording sits in IF DEFLECTED and is not a quotation of anyone
        f = fields(turn["body"])
        text = f.get("QUESTION", "") + "\n" + f.get("WHY I ASK", "")
    for quote, after in quotes(text):
        q = norm(quote)
        if turn["role"] == "Convict":
            if q not in convict_brain:
                out.append(Problem(tid, "quote-source", f'quote not found in the convict\'s brain: "{quote[:70]}..."'))
            if not re.match(r"\s*\((?:S|E)\d{3}", after):
                out.append(Problem(tid, "quote-source", f'quote has no id right after it (write "words" (S009, speaker, held date)): "{quote[:60]}..."'))
        elif turn["role"] == "Lawyer":
            if q not in lawyer_brain and q not in norm(earlier_text):
                out.append(Problem(tid, "quote-source", f'lawyer quote is in neither its own brain nor an earlier turn: "{quote[:70]}..."'))
        else:
            if q not in norm(earlier_text) and q not in norm(case_book):
                out.append(Problem(tid, "quote-source", f'judge quote is in neither the hearing nor the case book (did it open a brain?): "{quote[:70]}..."'))
    return out


def guard_ids(turn, convict_sources: dict, external_ids: set) -> list:
    if turn["role"] != "Convict":
        return []
    out, tid, body = [], turn["id"], turn["body"]
    if PLACEHOLDER_RE.search(body):
        out.append(Problem(tid, "id-exists", "placeholder id (S0xx) is not an id"))
    for m in ID_RE.finditer(body):
        i = m.group(1)
        if (i.startswith("S") and i not in convict_sources) or (i.startswith("E") and i not in external_ids):
            out.append(Problem(tid, "id-exists", f"{i} is not in the {'brain sources.md' if i.startswith('S') else 'external.md'}"))
    return out


def guard_no_speech_id(turn, speechless: set) -> list:
    out = []
    if turn["role"] == "Convict":
        for quote, after in quotes(turn["body"]):
            m = re.match(r"\s*\((S\d{3})", after)
            if m and m.group(1) in speechless:
                out.append(Problem(turn["id"], "no-speech-id", f"{m.group(1)} is not management speech, so nothing may be quoted from it"))
    return out


def guard_has_evidence(turn) -> list:
    if turn["role"] == "Convict" and re.match(r"^(A|WA|XA)\d+ ", turn["id"]):
        if not ID_RE.search(turn["body"]) and "not in my record" not in turn["body"].lower():
            return [Problem(turn["id"], "has-evidence", 'no id and no "not in my record"')]
    return []


def guard_number_date(turn) -> list:
    if turn["role"] != "Convict":
        return []
    out = []
    if turn["id"].startswith("Convict baseline"):
        # a baseline answer is one compressed line per question (under 60 words), so its date may sit a sentence away:
        # the window is the whole B-line, not 80 characters. A line with no date at all still fails.
        for line in turn["body"].splitlines():
            if re.match(r"B\d\d ANSWER:", line.strip()):
                for digits, pos in big_numbers(line):
                    if not DATE_WORDS.search(line):
                        out.append(Problem(turn["id"], "number-date", f"{digits} has no date, quarter or as-of word anywhere on its baseline line: {line.strip()[:20]}"))
        return out
    f = fields(turn["body"])
    text = (f.get("ANSWER", "") + "\n" + f.get("EVIDENCE", "")) if f else turn["body"]
    for digits, pos in big_numbers(text):
        window = text[max(0, pos - NUMBER_DATE_WINDOW):pos + len(digits) + NUMBER_DATE_WINDOW]
        if not DATE_WORDS.search(window):
            out.append(Problem(turn["id"], "number-date", f"{digits} has no date, quarter or as-of word within {NUMBER_DATE_WINDOW} characters"))
    return out


def guard_lawyer_numbers(turn, earlier_text: str, case_book: str) -> list:
    if turn["role"] != "Lawyer":
        return []
    known = {d for d, _ in big_numbers(case_book)} | {d for d, _ in big_numbers(earlier_text)}
    return [Problem(turn["id"], "lawyer-number", f"{d} is in neither the case book nor an earlier turn") for d, _ in big_numbers(turn["body"]) if d not in known]


def guard_external_ids(turn) -> list:
    if turn["role"] != "Convict":
        return []
    allowed_turn = turn["id"].startswith("Convict baseline")
    out = []
    for line in turn["body"].splitlines():
        if re.search(r"\bE\d{3}\b", line):
            external_line = "EXT" in line or (allowed_turn and re.match(r"\s*B(?:18|19|2[0-2])\b", line))
            if not external_line:
                out.append(Problem(turn["id"], "external-id", f"an external id on a line that is not an external point: {line.strip()[:70]}"))
    return out


def guard_judge(turn) -> list:
    if turn["role"] != "Judge":
        return []
    out, body, tid = [], turn["body"], turn["id"]
    for label in ("STORY SO FAR", "STORYLINE"):
        m = re.search(label + r":?\s*\n((?:\s*(?:\d+\.|-)\s.+\n?)+)", body)
        for line in (m.group(1).splitlines() if m else []):
            if line.strip() and not EVIDENCE_RE.search(line):
                out.append(Problem(tid, "judge-story", f"storyline line has no evidence id and no 'not in the record': {line.strip()[:70]}"))
            if words(line) > LIMITS["story_line_words"]:
                out.append(Problem(tid, "judge-story", f"storyline line is {words(line)} words, limit {LIMITS['story_line_words']}", "warn"))
    m = re.search(r"I DID NOT UNDERSTAND:?\s*\n?(.*?)(?:\n[A-Z][A-Z ]{6,}:|\Z)", body, re.S)
    if "I DID NOT UNDERSTAND" in body and (not m or not m.group(1).strip() or (m.group(1).strip().lower().startswith("none") and "because" not in m.group(1).lower())):
        out.append(Problem(tid, "judge-story", 'I DID NOT UNDERSTAND is empty or a bare "none" (a reason is needed)'))
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", re.sub(r"[-*|]", " ", body)) if len(s.split()) > 2]
    if sentences and sum(words(s) for s in sentences) / len(sentences) > 25:
        out.append(Problem(tid, "reading-level", f"sentences average {sum(words(s) for s in sentences) / len(sentences):.0f} words (a 15-year-old reads about 18)", "warn"))
    return out


# ---- running everything ---------------------------------------------------------------------------------------------------------------

def check(hearing: str, case_book: str, convict_brain_dir: Path, lawyer_brain_dir: Path, external: str = "") -> list:
    convict_text = norm(" ".join(p.read_text(encoding="utf-8", errors="replace") for p in convict_brain_dir.rglob("*.md")))
    lawyer_text = norm(" ".join(p.read_text(encoding="utf-8", errors="replace") for p in lawyer_brain_dir.rglob("*.md")))
    sources = sources_table((convict_brain_dir / "sources.md").read_text(encoding="utf-8")) if (convict_brain_dir / "sources.md").exists() else {}
    external_ids = set(re.findall(r"^#+\s*(E\d{3})\b|^- (E\d{3})\b", external, re.M)) if external else set()
    external_ids = {i for pair in external_ids for i in pair if i} | set(re.findall(r"\bE\d{3}\b", external))
    speechless = non_speech_ids(sources)
    problems, earlier = [], ""
    for turn in parse_turns(hearing):
        problems += guard_turn_shape(turn)
        problems += guard_quotes(turn, earlier, case_book, convict_text, lawyer_text)
        problems += guard_ids(turn, sources, external_ids)
        problems += guard_no_speech_id(turn, speechless)
        problems += guard_has_evidence(turn)
        problems += guard_number_date(turn)
        problems += guard_lawyer_numbers(turn, earlier, case_book)
        problems += guard_external_ids(turn)
        problems += guard_judge(turn)
        earlier += "\n" + turn["body"]
    return problems


def main() -> int:
    session = Path(sys.argv[1])
    case = json.loads((session / "case.json").read_text(encoding="utf-8"))
    external = (session / "external.md").read_text(encoding="utf-8") if (session / "external.md").exists() else ""
    problems = check((session / "hearing.md").read_text(encoding="utf-8"), (session / "case-book.md").read_text(encoding="utf-8"),
                     BRAINS / case.get("convict_brain", "biocon-management"), BRAINS / case.get("lawyer_brain", "india-market-analyst"), external)
    for p in problems:
        print(p)
    fails = sum(p.severity == "FAIL" for p in problems)
    print(f"{fails} problem(s) to fix, {len(problems) - fails} warning(s)")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
