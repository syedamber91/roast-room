#!/usr/bin/env python3
"""Turn a finished hearing into the decision, the numbers behind it, and one HTML page.

    python build_report.py <session> --gates none --price-on-file --results-on-file
    python build_report.py <session> --ceilings          # print the ceilings and the rule's position, then stop

Reads (all inside the session folder): case.json, case-book.md, hearing.md, external.md (optional).
Reads the convict's brain only for three counts the case book does not hold (promise scorecard,
how each call's questions were answered, votes against). It never reads a brain for a fact the judge sees.
Writes: dashboard.json, report.md, report.html, reader-card.html (the decision card alone, for the reader test) and reader-test-sheet.md.

The judge's words are shown as written. Every number on a chart comes from a table of the case book or
from a brain table, with its source named, and a missing source draws "not in the record", never a guess.
"""

import argparse
import importlib.util
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
BRAINS = HERE.parents[1] / "roast-room" / "brains"
TEMPLATE = HERE / "report_template.html"
MARKER = "/*DASHBOARD_JSON*/"


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rules = load("court_rules")
chk = load("check_hearing")


# ---- reading markdown tables ----------------------------------------------------------------------------------------------------------

def tables(text):
    """[(label, [header cells], [[row cells]])] for every markdown table, in order. The label is the last '#' heading plus the last text line above the table."""
    out, heading, above, lines = [], "", "", text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            heading = line.lstrip("# ").strip()
        elif line.strip() and not line.startswith("|"):
            above = line.strip()   # the paragraph right above a table often names it
        if line.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:\-|]+\|$", lines[i + 1].strip()):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            rows, i = [], i + 2
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append((heading + " | " + above, header, rows))
            continue
        i += 1
    return out


def number(cell):
    """A table cell as a number, or None. Handles commas, a leading plus, and 'nil (...)'."""
    cell = cell.strip()
    if cell.lower().startswith("nil"):
        return 0.0
    m = re.match(r"^\(?([+-]?[\d,]+(?:\.\d+)?)\)?", cell)
    if not m:
        return None
    value = float(m.group(1).replace(",", ""))
    return -value if cell.startswith("(") else value


def find_table(all_tables, heading_part, must_have):
    for heading, header, rows in all_tables:
        if heading_part.lower() in heading.lower() and all(any(h.lower().startswith(m.lower()) for h in header) for m in must_have):
            return header, rows
    return None


def column(header, start):
    for i, h in enumerate(header):
        if h.lower().startswith(start.lower()):
            return i
    return None


# ---- chart data, one function per exhibit ---------------------------------------------------------------------------------------------

def quarters_data(case_book):
    """Quarterly sales, margin and segment sales, joined by quarter-end date. None when the tables are missing."""
    all_t = tables(case_book)
    q = find_table(all_t, "Filed quarters", ["Quarter ended", "Revenue from operations"])
    s = find_table(all_t, "Segments", ["Quarter ended", "Generics"])
    if not q:
        return None, []
    hq, rq = q
    d, rev, mar = column(hq, "Quarter ended"), column(hq, "Revenue from operations"), column(hq, "Operating margin %")
    segs = {}
    breaks = []
    if s:
        hs, rs = s
        date_i, gen_i, bio_i = column(hs, "Quarter ended"), column(hs, "Generics"), column(hs, "Biosimilars")
        name_i = column(hs, "Third segment (name")
        amount_i = hs.index("Third segment")   # the header whose whole text is exactly this
        for row in rs:
            segs[row[date_i]] = {"gen": number(row[gen_i]), "bio": number(row[bio_i]), "third": number(row[amount_i])}
        for before, now in zip(rs, rs[1:]):
            if before[name_i] != now[name_i]:
                breaks.append({"date": now[date_i], "label": "third segment now called " + now[name_i]})
    rows = []
    for row in rq:
        date = row[d]
        seg = segs.get(date, {})
        rows.append({"date": date, "rev": number(row[rev]), "margin": number(row[mar]) if mar is not None else None,
                     "gen": seg.get("gen"), "bio": seg.get("bio"), "third": seg.get("third")})
    return rows, breaks


def basis_changed(case_book):
    return bool(re.search(r"not on the same basis", case_book))


def debt_data(case_book):
    t = find_table(tables(case_book), "Borrowings by when they fall due", ["Falls due"])
    if not t:
        return None
    header, rows = t
    return {"now_label": header[1], "prev_label": header[2],
            "bands": [{"band": r[0], "now": number(r[1]), "prev": number(r[2])} for r in rows if r[0].lower() != "total"],
            "totals": [number(r[1]) for r in rows if r[0].lower() == "total"] + [number(r[2]) for r in rows if r[0].lower() == "total"]}


def holdings_data(case_book):
    t = find_table(tables(case_book), "Promoter and public shareholding", ["Period", "Promoter %"])
    if not t:
        return None
    header, rows = t
    p, pc, ts, pl = column(header, "Period"), column(header, "Promoter %"), column(header, "Implied total shares"), column(header, "Pledged flag")
    return [{"period": r[p], "promoter_pct": number(r[pc]), "total_shares_m": (number(r[ts]) or 0) / 1e6, "pledged": r[pl]} for r in rows]


def calls_data(brain_dir):
    f = brain_dir / "qa-states.md"
    if not f.exists():
        return None
    t = find_table(tables(f.read_text(encoding="utf-8")), "Counts per call", ["Call held"])
    if not t:
        return None
    header, rows = t
    keys = ["answered", "partial", "deflected", "declined", "deferred", "no answer turn", "unverified", "not judged"]
    cols = {k: column(header, k) for k in keys}
    out = []
    for r in rows:
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", r[0]):
            continue
        out.append({"date": r[0], "source": r[1], **{k: int(number(r[cols[k]]) or 0) for k in keys}})
    return out


def votes_data(brain_dir):
    f = brain_dir / "votes.md"
    if not f.exists():
        return None
    t = find_table(tables(f.read_text(encoding="utf-8")), "Related party resolutions by meeting", ["Meeting"])
    if not t:
        return None
    header, rows = t
    m, a = column(header, "Meeting"), column(header, "Highest % against (all votes)")
    return [{"meeting": r[m], "max_against": number(r[a])} for r in rows]


def promises_data(brain_dir):
    f = brain_dir / "record.md"
    if not f.exists():
        return None
    m = re.search(r"Totals: Kept (\d+), Missed (\d+), Still open (\d+), Depends on reading (\d+)", f.read_text(encoding="utf-8"))
    return dict(zip(["kept", "missed", "open", "depends"], map(int, m.groups()))) if m else None


# ---- the decision ---------------------------------------------------------------------------------------------------------------------

def last_final(turns):
    finals = [t for t in turns if t["id"].lower().startswith("judge final")]
    return finals[-1]["body"] if finals else None


def section_inputs(case):
    """{S1: [decisive ids], ...} and {S1: [all analyst question ids], ...} from the case's issues."""
    decisive, allowed = {}, {}
    for issue in case["issues"]:
        s = issue.get("section")
        if s:
            decisive.setdefault(s, []).append(issue["decisive"])
            allowed.setdefault(s, set()).update(issue["analyst_questions"])
    return decisive, allowed


def build_decision(final, case, gates, price_on_file, results_on_file, no_guidance):
    """The judge's final turn run through the rules. Returns (decision dict, problems list)."""
    problems = []
    decisive, allowed = section_inputs(case)
    ceilings = {}
    for s in rules.SECTIONS:
        states = final["states"].get(s, {})
        for qid in states:
            if qid not in allowed.get(s, set()):
                problems.append("%s lists %s, which is not one of its questions" % (s, qid))
        ceilings[s] = rules.section_ceiling(states, decisive.get(s, []), no_guidance if s == "S1" else None)
    rows = rules.cap_scores(final["scores"], ceilings)
    total = rules.trust_total(rows)
    computed, why = rules.compute_position(total, gates, price_on_file, results_on_file)
    position, note = rules.apply_judge_position(computed, final["position"])
    if final["position"] is None:
        problems.append("the judge's POSITION line is missing or not one of the four words")
    heard = [s for s in rules.SECTIONS if ceilings[s][0] > 0 or final["states"].get(s)]
    for r in rows:
        r["states"] = final["states"].get(r["section"], {})
        r["why"] = final["why"].get(r["section"], "")
        if r["cut"]:
            problems.append("judge-ceiling: " + r["section"] + ": " + r["cut"])
    problems += rules.reader_line_problems(position, final["reader_not_own"][0])
    if len(final["triggers"]) > 3:
        problems.append("more than three triggers")
    if len(final["storyline"]) != 10:
        problems.append("storyline has %d lines, not 10" % len(final["storyline"]))
    for head in final["missing"]:
        problems.append("the judge's final turn has no %s part" % head)
    return {
        "scores": rows, "total": total, "band": rules.band_of(total),
        "rule_position": {"key": computed, "label": rules.POSITION_LABEL[computed], "reasons": why},
        "position": {"key": position, "label": rules.POSITION_LABEL[position], "judge_note": note, "judge_reason": final["position_reason"]},
        "sections_with_data": len([s for s in heard]),
        "direction": final["direction"], "direction_why": final["direction_why"],
        "reader_not_own": {"word": final["reader_not_own"][0], "change": final["reader_not_own"][1]},
        "reader_own": {"word": final["reader_own"][0], "change": final["reader_own"][1]},
        "triggers": final["triggers"][:3], "not_decided": final["not_decided"], "red_flags": final["red_flags"],
        "storyline": final["storyline"], "glossary": final["glossary"], "defence": final["defence"],
        "gates": sorted(gates), "price_on_file": price_on_file, "results_on_file": results_on_file,
    }, problems


def hearing_panels(turns):
    """Group the hearing's turns by section heading, keeping their text as written."""
    panels, index = [], {}
    for t in turns:
        if t["id"].lower().startswith("judge final"):
            continue
        key = t["section"] or "Hearing"
        if key not in index:
            index[key] = len(panels)
            panels.append({"title": key, "turns": []})
        state = re.search(r"STATE I CLAIM:\s*([a-z ]+)", t["body"])
        panels[index[key]]["turns"].append({"id": t["id"], "role": t["role"], "text": t["body"], "state": state.group(1).strip() if state else None})
    return panels


def facts_line(case, decision, problems):
    gap_count = len(case.get("not_in_record", []))
    return "%d of 7 sections had data. %d gaps are listed as not in the record. %d notes from the checks. The bands are the seat's own and untested." % (
        decision["sections_with_data"], gap_count, len(problems))


# ---- writing --------------------------------------------------------------------------------------------------------------------------

def as_of_pills(case):
    out = [("Run date", case["run_date"])]
    if case.get("announcements_to"):
        out.append(("Exchange feed to", case["announcements_to"]))
    return [{"label": a, "value": b} for a, b in out]


def render_markdown(case, d, problems):
    lines = ["# %s: the court's decision" % case["company"], "",
             "Simulation, not advice, and not a SEBI-registered adviser. Run %s." % case["run_date"], "",
             "**Position: %s.** %s" % (d["position"]["label"], " ".join(d["rule_position"]["reasons"])), ""]
    if d["position"]["judge_note"]:
        lines += [d["position"]["judge_note"] + ".", ""]
    lines += ["Trust %d of 21 (band %s, %s). Direction: %s." % (d["total"], d["band"]["range"], d["band"]["caveat"], d["direction"] or "not given"), "",
              "| Section | Judge | Ceiling | Final |", "|---|---|---|---|"]
    for r in d["scores"]:
        lines.append("| %s %s | %s | %d | %d |" % (r["section"], r["name"], "-" if r["judge"] is None else r["judge"], r["ceiling"], r["final"]))
    lines += ["", "If you do not own it: %s. %s" % (d["reader_not_own"]["word"], d["reader_not_own"]["change"]),
              "If you own it: %s. %s" % (d["reader_own"]["word"], d["reader_own"]["change"]), "", "Triggers:"]
    lines += ["- %s | %s | moves %s" % (t["when"], t["check"], t["moves"]) for t in d["triggers"]]
    lines += ["", "What this does not decide:"] + ["- " + x for x in d["not_decided"]]
    if problems:
        lines += ["", "Checks that need a look:"] + ["- " + p for p in problems]
    return "\n".join(lines) + "\n"


READER_QUESTIONS = ["What is the position, in your own words?", "Why, in two or three sentences?", "What would change it?",
                    "What does this page not decide?", "What would you check next?"]


def reader_test_sheet(case, d):
    """Test 4 of the design: a reader sees only reader-card.html and answers five questions. This is the scorer's sheet with the key."""
    lines = ["# Reader test: %s" % case["company"], "",
             "Give the reader ONLY `reader-card.html`. No charts, no hearing, no help. Ask the five questions and write the answers down. "
             "Score one point for each answer that matches the key in meaning, not wording. Pass bar, fixed before any reader: 4 of 5, in 5 minutes or less.", "",
             "| # | Question | Key (scorer only) |", "|---|---|---|",
             "| 1 | %s | %s |" % (READER_QUESTIONS[0], d["position"]["label"]),
             "| 2 | %s | %s |" % (READER_QUESTIONS[1], (" ".join(d["rule_position"]["reasons"]) + " " + (d["position"]["judge_reason"] or "")).strip()),
             "| 3 | %s | not owner: %s; owner: %s |" % (READER_QUESTIONS[2], d["reader_not_own"]["change"], d["reader_own"]["change"]),
             "| 4 | %s | %s |" % (READER_QUESTIONS[3], "; ".join(d["not_decided"][:4])),
             "| 5 | %s | %s |" % (READER_QUESTIONS[4], "; ".join("%s (%s)" % (t["when"], t["check"]) for t in d["triggers"]) or "no trigger was named"),
             "", "Reader score: ___ of 5. Minutes taken: ___. What was unclear: ___"]
    return "\n".join(lines).replace("|  |", "| |") + "\n"


def build(session, gates, price_on_file, results_on_file, no_guidance):
    case = json.loads((session / "case.json").read_text(encoding="utf-8"))
    case_book = (session / "case-book.md").read_text(encoding="utf-8")
    hearing = (session / "hearing.md").read_text(encoding="utf-8")
    external = (session / "external.md").read_text(encoding="utf-8") if (session / "external.md").exists() else ""
    turns = chk.parse_turns(hearing)
    final_text = last_final(turns)
    if final_text is None:
        raise SystemExit("hearing.md has no '### Judge final' turn yet")
    convict_dir = BRAINS / case.get("convict_brain", "")
    decision, problems = build_decision(rules.parse_final(final_text), case, gates, price_on_file, results_on_file, no_guidance)
    problems += [str(p) for p in chk.check(hearing, case_book, convict_dir, BRAINS / case.get("lawyer_brain", ""), external)]
    quarters, breaks = quarters_data(case_book)
    dashboard = {
        "company": case["company"], "run_date": case["run_date"], "as_of": as_of_pills(case), "gate": case.get("gate"),
        "decision": decision, "facts_line": facts_line(case, decision, problems), "problems": problems,
        "exhibits": {"quarters": quarters, "breaks": breaks, "basis_changed": basis_changed(case_book), "promises": promises_data(convict_dir),
                     "calls": calls_data(convict_dir), "debt": debt_data(case_book), "holdings": holdings_data(case_book), "votes": votes_data(convict_dir)},
        "hearing": hearing_panels(turns), "not_in_record": case.get("not_in_record", []),
    }
    return dashboard, problems, case


def write_all(session, dashboard, problems, case):
    (session / "dashboard.json").write_text(json.dumps(dashboard, indent=1), encoding="utf-8")
    (session / "report.md").write_text(render_markdown(case, dashboard["decision"], problems), encoding="utf-8")
    page = TEMPLATE.read_text(encoding="utf-8")
    safe = json.dumps(dashboard).replace("<", "\\u003c")
    full = page.replace(MARKER, safe)
    (session / "report.html").write_text(full, encoding="utf-8")
    (session / "reader-card.html").write_text(full.replace('data-level="full"', 'data-level="card"', 1), encoding="utf-8")
    (session / "reader-test-sheet.md").write_text(reader_test_sheet(case, dashboard["decision"]), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("session")
    ap.add_argument("--gates", default="none", help="comma list of gates the Chair confirmed, for example G-E, or none")
    ap.add_argument("--price-on-file", action="store_true")
    ap.add_argument("--results-on-file", action="store_true")
    ap.add_argument("--no-guidance", choices=["numeric", "none"], default=None, help="S1 special case, set by the Chair")
    ap.add_argument("--ceilings", action="store_true", help="print the ceilings and the rule's position, then stop")
    a = ap.parse_args()
    gates = set() if a.gates == "none" else {g.strip() for g in a.gates.split(",")}
    session = Path(a.session)
    dashboard, problems, case = build(session, gates, a.price_on_file, a.results_on_file, a.no_guidance)
    d = dashboard["decision"]
    if a.ceilings:
        for r in d["scores"]:
            print("%s ceiling %d (%s)" % (r["section"], r["ceiling"], r["ceiling_why"]))
        print("rule position: %s (%s)" % (d["rule_position"]["label"], "; ".join(d["rule_position"]["reasons"])))
        return 0
    write_all(session, dashboard, problems, case)
    for p in problems:
        print(p)
    print("wrote dashboard.json, report.md, report.html: position %s, trust %d of 21, %d note(s)" % (d["position"]["label"], d["total"], len(problems)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
