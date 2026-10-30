"""The courtroom's rules, written as plain functions so a test can prove each one.

Nothing here reads a brain or calls a model. It takes what the judge wrote in the
final turn and the facts the Chair supplies (gates, price on file, results on file),
and works out three things:

1. a ceiling for each trust section, from the states of its core questions;
2. the position the council's stock rating rule allows;
3. the cut-down report: where the judge said more than the evidence allows.

The rule text lives in .claude/skills/roast-room/references/stock-rating.md.
The bands are the seat's own, uncalibrated, and every printed band says so.
"""

import re

STATES = ["answered", "partial", "deflected", "no data", "unverified"]
# Used only to pick the LOWER reading when a blind second reader disputes a state.
STATE_RANK = {"answered": 3, "partial": 2, "deflected": 1, "no data": 0, "unverified": 0}

SECTIONS = ["S1", "S2", "S3", "S4", "S5", "S6", "S7"]
SECTION_NAMES = {
    "S1": "Guidance against delivery",
    "S2": "Earnings quality and accounting",
    "S3": "Cash, receivables, working capital",
    "S4": "Debt and funding",
    "S5": "Related parties and group companies",
    "S6": "Promoter: pledge, selling, succession",
    "S7": "Board, auditors, independent directors",
}

BANDS = [(18, 21, "18 to 21", "answered and clean"), (12, 17, "12 to 17", "answered with open flags"),
         (7, 11, "7 to 11", "mostly partial"), (0, 6, "0 to 6", "unanswered or declined")]
BAND_CAVEAT = "seat's own bands, not from any source, uncalibrated"

# Position, best first. The judge may move down this list, never up.
POSITIONS = ["buy", "wait_good", "wait", "avoid"]
POSITION_LABEL = {"buy": "Buy", "wait_good": "Wait: trust good, entry not yet", "wait": "Wait", "avoid": "Avoid"}
HARD_GATES = {"G-A", "G-B", "G-C", "G-D"}   # each sets Sell leans to 7 or more
CAP_GATE = "G-E"                             # caps at Wait


def lowest_state(states):
    """The lowest reading of a list of states (used when a question is disputed)."""
    return min(states, key=lambda s: STATE_RANK[s])


def section_ceiling(states, decisive, no_guidance=None):
    """Ceiling for one section.

    states: {"Q1.1": "answered", ...} for the core questions the court heard in this section.
    decisive: the question ids that decide the section (from issues.json).
    no_guidance: None when the rule does not apply, "numeric" when the company states a
        no-guidance policy and gives another numeric anchor, "none" when it gives none.
        It only matters for S1 and the Chair sets it, never the judge.
    Returns (ceiling 0 to 3, one plain reason).
    """
    if no_guidance in ("numeric", "none"):
        value = 2 if no_guidance == "numeric" else 1
        why = ("states a no-guidance policy and gives another numeric anchor" if value == 2
               else "states a no-guidance policy and gives no other numeric anchor")
        return value, why + " (council ladder, S1 special case)"
    heard = {q: states[q] for q in decisive if q in states}
    if not heard or len(heard) < len(decisive):
        missing = [q for q in decisive if q not in states]
        return 0, "the deciding question " + " and ".join(missing) + " was not heard"
    worst = lowest_state(list(heard.values()))
    others = [s for q, s in states.items() if q not in decisive]
    if worst == "answered":
        if all(s == "answered" for s in others):
            return 3, "every core question answered with a number and a date"
        slipped = sorted(q for q, s in states.items() if q not in decisive and s != "answered")
        return 2, "the deciding question was answered but " + ", ".join(slipped) + " was not"
    if worst == "partial":
        return 1, "the deciding question got words but no number"
    return 0, "the deciding question was " + worst


def cap_scores(judge_scores, ceilings):
    """Cut every judge score down to its ceiling.

    judge_scores: {"S1": 3, ...}; ceilings: {"S1": (2, "reason"), ...}.
    Returns a list of rows with the final number and, where cut, the sentence to print.
    """
    rows = []
    for s in SECTIONS:
        said = judge_scores.get(s)
        ceil, why = ceilings.get(s, (0, "section not heard"))
        if said is None:
            final, cut = 0, None
            note = "the judge gave no number; counted as 0"
        else:
            final = min(said, ceil)
            cut = None
            note = ""
            if said > ceil:
                cut = "judge said %d, evidence allows %d, because %s" % (said, ceil, why)
        rows.append({"section": s, "name": SECTION_NAMES[s], "judge": said, "ceiling": ceil,
                     "ceiling_why": why, "final": final, "cut": cut, "note": note})
    return rows


def trust_total(rows):
    return sum(r["final"] for r in rows)


def band_of(total):
    for lo, hi, name, meaning in BANDS:
        if lo <= total <= hi:
            return {"range": name, "meaning": meaning, "caveat": BAND_CAVEAT}
    raise ValueError("trust total out of range: %r" % total)


def compute_position(total, gates, price_on_file, results_on_file):
    """The position the stock rating rule allows. Returns (key, reasons)."""
    gates = set(gates or [])
    hard = sorted(gates & HARD_GATES)
    if hard:
        return "avoid", ["gate " + ", ".join(hard) + " stands: a finding or invoked pledge puts Sell at 7 or more"]
    if CAP_GATE in gates:
        return "wait", ["gate G-E stands: an interim order or unvalidated first estimate caps the position at Wait"]
    entry_missing = [n for n, ok in (("a current price", price_on_file), ("the latest results", results_on_file)) if not ok]
    if total >= 18 and not entry_missing:
        return "buy", ["no gate, trust %d is in the 18 to 21 band, price and results are on file" % total]
    if total >= 12 and entry_missing:
        return "wait_good", ["trust %d is 12 or more with no gate; held at Wait only because %s is not on file" % (total, " and ".join(entry_missing))]
    if total >= 18:
        return "wait", ["trust %d clears the bar but the position is held at Wait" % total]
    return "wait", ["trust %d is below the 18 to 21 band, so Buy is not allowed" % total]


def apply_judge_position(computed, judge_choice):
    """The judge may move the position down, never up. Returns (final key, note or None)."""
    if judge_choice is None or judge_choice == computed:
        return computed, None
    if judge_choice not in POSITIONS:
        return computed, "judge wrote an unknown position %r; the rule's position stands" % judge_choice
    if POSITIONS.index(judge_choice) < POSITIONS.index(computed):
        return computed, "judge asked for %s, the rule allows at most %s; the rule's position stands" % (
            POSITION_LABEL[judge_choice], POSITION_LABEL[computed])
    return judge_choice, "judge moved the position down from %s to %s" % (POSITION_LABEL[computed], POSITION_LABEL[judge_choice])


NOT_OWN_WORDS = {"buy": "Buy", "wait_good": "Wait: trust good, entry not yet", "wait": "Wait", "avoid": "Avoid"}


def reader_line_problems(position, not_own_word):
    """The line for a reader who does not own the stock may say Buy only when the rule's final position is Buy."""
    problems = []
    word = (not_own_word or "").strip().lower()
    if word.startswith("buy") and position != "buy":
        problems.append("reader line says Buy but the position is %s" % POSITION_LABEL[position])
    if position == "avoid" and word.startswith("wait"):
        problems.append("reader line says Wait but the position is Avoid")
    return problems


# ---------------------------------------------------------------- final turn

HEADS = ["SECTION SCORES", "DIRECTION", "DIRECTION WHY", "RED FLAGS", "POSITION", "READER NOT OWN", "READER OWN",
         "TRIGGERS", "NOT DECIDED", "STORYLINE", "GLOSSARY", "WHY THE DEFENCE HELD OR DID NOT"]
HEAD_RE = re.compile(r"^(" + "|".join(HEADS) + r"):[ \t]*(.*)$", re.M)
DIRECTIONS = {"improving", "mixed", "worsening", "can't tell"}


def split_final(text):
    """Split the judge's final turn into {HEAD: body}. Returns {} if there is no head at all."""
    marks = list(HEAD_RE.finditer(text))
    out = {}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        out[m.group(1)] = (m.group(2) + "\n" + text[m.end():end]).strip()
    return out


def parse_scores(body):
    """Lines of the form `S1 | 2 | states: Q1.1 answered, Q1.2 partial | WHY: text`."""
    scores, states, why = {}, {}, {}
    for line in body.splitlines():
        m = re.match(r"^-?\s*(S[1-7])\s*\|\s*([0-3])\s*\|\s*states:\s*(.*?)\s*\|\s*WHY:\s*(.*)$", line.strip())
        if not m:
            continue
        sec = m.group(1)
        scores[sec] = int(m.group(2))
        why[sec] = m.group(4).strip()
        states[sec] = {}
        for qid, st in re.findall(r"(Q\d+\.\d+)\s+(answered|partial|deflected|no data|unverified)", m.group(3)):
            states[sec][qid] = st
    return scores, states, why


def parse_position(body):
    """`POSITION: Wait | MOVE DOWN FROM RULE: no | REASON: ...` returns (key or None, reason)."""
    first = body.splitlines()[0] if body else ""
    word = first.split("|")[0].strip().lower()
    key = None
    for k, label in POSITION_LABEL.items():
        if word == label.lower():
            key = k
    reason = ""
    m = re.search(r"REASON:\s*(.*)", body)
    if m:
        reason = m.group(1).strip()
    return key, reason


def parse_reader(body):
    """`Wait | what would change it: ...` returns (word, change)."""
    first = body.splitlines()[0] if body else ""
    parts = [p.strip() for p in first.split("|", 1)]
    return parts[0], (parts[1] if len(parts) > 1 else "")


def parse_triggers(body):
    """`1. event or date | check: ... | moves: up|down|either` returns a list of dicts."""
    out = []
    for line in body.splitlines():
        m = re.match(r"^\s*\d+\.\s*(.*?)\s*\|\s*check:\s*(.*?)\s*\|\s*moves:\s*(up|down|either)\b", line, re.I)
        if m:
            out.append({"when": m.group(1), "check": m.group(2), "moves": m.group(3).lower()})
    return out


def parse_numbered(body):
    return [re.sub(r"^\s*\d+\.\s*", "", l).strip() for l in body.splitlines() if re.match(r"^\s*\d+\.\s+\S", l)]


def parse_glossary(body):
    out = []
    for line in body.splitlines():
        m = re.match(r"^-?\s*([^:]{2,40}):\s+(.+)$", line.strip())
        if m:
            out.append({"term": m.group(1).strip(), "meaning": m.group(2).strip()})
    return out


def parse_flags(body):
    """`- Q2.3 | the claim | evidence id` returns a list of dicts."""
    out = []
    for line in body.splitlines():
        parts = [p.strip() for p in line.lstrip("- ").split("|")]
        if len(parts) >= 3 and re.match(r"^Q\d+\.\d+$", parts[0]):
            out.append({"question": parts[0], "flag": parts[1], "evidence": parts[2]})
    return out


def parse_final(text):
    """The judge's final turn as a dict. Missing parts are None, never guessed."""
    parts = split_final(text)
    scores, states, why = parse_scores(parts.get("SECTION SCORES", ""))
    position_key, position_reason = parse_position(parts.get("POSITION", ""))
    direction = (parts.get("DIRECTION", "").splitlines() or [""])[0].strip().lower()
    return {
        "scores": scores, "states": states, "why": why,
        "direction": direction if direction in DIRECTIONS else None,
        "direction_why": parts.get("DIRECTION WHY"),
        "red_flags": parse_flags(parts.get("RED FLAGS", "")),
        "position": position_key, "position_reason": position_reason,
        "reader_not_own": parse_reader(parts.get("READER NOT OWN", "")),
        "reader_own": parse_reader(parts.get("READER OWN", "")),
        "triggers": parse_triggers(parts.get("TRIGGERS", "")),
        "not_decided": [l.lstrip("- ").strip() for l in parts.get("NOT DECIDED", "").splitlines() if l.strip()],
        "storyline": parse_numbered(parts.get("STORYLINE", "")),
        "glossary": parse_glossary(parts.get("GLOSSARY", "")),
        "defence": parts.get("WHY THE DEFENCE HELD OR DID NOT"),
        "missing": [h for h in HEADS if h not in parts],
    }
