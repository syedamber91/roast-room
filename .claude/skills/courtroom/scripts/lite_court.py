#!/usr/bin/env python3
"""LITE courtroom: a cheap hearing built from already-answered, already-code-checked data-point answers.

    python lite_court.py --answers <t6-ask-....md> --out <dir> [--company "PI Industries (PIIND)"] [--judge auto|nemotron|none]

Reads the answers file written by the VPS data-point run (`Q: ...` then `  ANSWER: figure  (source cite)` or `  REFUSE: reason`).
Writes lite-report.html, lite-receipts.html and lite-result.json into <dir>.

Who does what:
- the questions are FIXED (the data-point questions; no model writes them);
- the answers are the VPS run's answers; answered / refused is set here by CODE, never by a model;
- the judge (Nemotron, via nvidia_client.py) only writes short notes and may only LOWER a section score; each note's quote is
  checked by code to appear in the answers, rewritten once if not, dropped if still not;
- ceilings, trust total, band and position come from court_rules.py;
- gates are NOT checked. Not comparable to the full BIOCON hearing.
"""
import argparse
import html
import importlib.util
import json
import os
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REFS = HERE.parent / "references"
MODEL = "nvidia/nemotron-3-ultra-550b-a55b"


def _load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


rules = _load("court_rules")

# ---------------------------------------------------------------- reading the answers

Q_RE = re.compile(r"^Q:\s*(.*\S)\s*$")
A_RE = re.compile(r"^\s+ANSWER:\s*(.*?)\s*\(([^()]*?)\s+(p\d+)\)\s*$")
R_RE = re.compile(r"^\s+REFUSE:\s*(.*\S)\s*$")


def parse_answers(text, control=()):
    """List of {n, question, state, figure, source, cite, reason}. state: answered | refused | control.

    An ANSWER line without a source and a page counts as refused (nothing to check it against).
    A control question that is answered stops the run: the control must stay refused.
    """
    rows, cur = [], None
    for line in text.splitlines():
        m = Q_RE.match(line)
        if m:
            cur = {"n": len(rows) + 1, "question": m.group(1), "state": "refused", "figure": "", "source": "",
                   "cite": "", "reason": "no answer line"}
            rows.append(cur)
            continue
        if cur is None:
            continue
        a = A_RE.match(line)
        if a:
            cur.update(state="answered", figure=a.group(1), source=a.group(2), cite=a.group(3), reason="")
            continue
        r = R_RE.match(line)
        if r:
            cur["reason"] = r.group(1)
    for row in rows:
        if row["n"] in control:
            if row["state"] == "answered":
                raise ValueError("control question %d was answered; the control must stay refused, so this run is not valid" % row["n"])
            row["state"] = "control"
    return rows


# ---------------------------------------------------------------- judge notes

def _norm(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def _haystack(rows):
    return _norm(" ".join("%s %s %s %s ; %s (%s %s)" % (r["question"], r["figure"], r["source"], r["cite"],
                                                          r["figure"], r["source"], r["cite"]) for r in rows))


def quote_ok(quote, rows):
    q = _norm(quote)
    return len(q) >= 3 and q in _haystack(rows)


NUM_RE = re.compile(r"(?<![A-Za-z0-9.])\d[\d,]*(?:\.\d+)?")
ANY_NUM_RE = re.compile(r"\d[\d,]*(?:\.\d+)?")


def _num(tok):
    return tok.replace(",", "").rstrip(".")


def numbers_ok(note, rows):
    """Every standalone number in a note must be written in the answers or questions. A figure the model worked out
    itself (a percent change, a difference) is not in the evidence, so the note fails."""
    have = {_num(t) for t in ANY_NUM_RE.findall(" ".join("%s %s %s %s" % (r["question"], r["figure"], r["source"], r["cite"]) for r in rows))}
    return all(_num(t) in have for t in NUM_RE.findall(note))


def _answers_block(rows):
    return "\n".join('- Q%d: %s | ANSWER: %s (%s %s)' % (r["n"], r["question"], r["figure"], r["source"], r["cite"])
                     for r in rows if r["state"] == "answered")


def judge_prompt(iid, name, rows):
    return ("ISSUE %s: %s\n"
            "You are the judge in a lite courtroom. Below are the ONLY facts: answers to fixed data-point questions, each with a figure and a page cite.\n"
            "The evidence is single figures on purpose. Missing detail is not a reason to score low: do not mark an issue down because covenants, "
            "segments or commentary are absent. Judge only what is there.\n"
            "Write 1 to 3 short plain notes on what these figures show or whether any look odd or contradict each other. "
            "Use only numbers written in the answers below. Do not calculate percentages, differences or ratios, and do not invent any figure; "
            "say \"fell\" or \"rose\" in words instead.\n"
            "Each note needs a QUOTE: copy 1 to 8 words, letter for letter, from a FIGURE or a QUESTION below (for example 17,023 Rs million). "
            "No brackets, no changes, no joining two answers.\n"
            "Then give one SCORE from 0 to 3 for how far these figures support a reader on this issue: "
            "3 = the figures are complete and consistent for the issue's questions; 2 = usable with a small oddity; "
            "1 = the figures are thin or only loosely about the issue; 0 = they contradict each other or are unusable. "
            "You may only be strict, never generous: if unsure, pick the lower number.\n"
            "Format, nothing else:\nNOTE: <one sentence>\nQUOTE: \"<exact text>\"\n(repeat)\nSCORE: <0-3>\n\n%s\n"
            % (iid, name, _answers_block(rows)))


def parse_judge(text):
    """({notes:[{note, quote}], score or None})."""
    notes, cur, score = [], None, None
    for line in text.splitlines():
        line = line.strip()
        if line.upper().startswith("NOTE:"):
            cur = {"note": line[5:].strip(), "quote": ""}
            notes.append(cur)
        elif line.upper().startswith("QUOTE:") and cur is not None:
            cur["quote"] = line[6:].strip().strip('"').strip("\u201c\u201d").strip()
        elif line.upper().startswith("SCORE:"):
            m = re.search(r"[0-3]", line[6:])
            score = int(m.group(0)) if m else score
    return notes, score


def judge_issue(iid, name, rows, generate):
    """Run the judge for one issue. Returns {notes, dropped, score, raw, rejected}. Failed quotes: one rewrite, then dropped.
    raw (the model's replies) and rejected (the quotes that were not found) are kept so a dropped note can be diagnosed."""
    prompt = judge_prompt(iid, name, rows)
    raw = [generate(prompt)]
    notes, score = parse_judge(raw[0])
    def accepted(n):
        return bool(n["quote"]) and quote_ok(n["quote"], rows) and numbers_ok(n["note"], rows)

    good = [n for n in notes if accepted(n)]
    bad = [n for n in notes if n not in good]
    rejected = [n["quote"] or n["note"] for n in bad]
    bad_left = 0
    if bad:
        retry = prompt + ("\nNOT ACCEPTED (quote not found in the answers, or a number in the note is not written in the answers): %s\n"
                          "Rewrite only those notes: copy exact text for the QUOTE, use only numbers written in the answers, calculate nothing. "
                          "Same format.\n" % "; ".join('"%s"' % (n["note"]) for n in bad))
        raw.append(generate(retry))
        again, score2 = parse_judge(raw[1])
        fixed = [n for n in again if accepted(n)]
        rejected += [n["quote"] or n["note"] for n in again if n not in fixed]
        good += fixed[:len(bad)]
        bad_left = len(bad) - len(fixed[:len(bad)])
        score = score if score is not None else score2
    return {"notes": good, "dropped": bad_left, "score": score, "raw": raw, "rejected": rejected}


# ---------------------------------------------------------------- the hearing

def _lite_why(text):
    text = text.replace("the deciding question none was not heard", "no data-point question maps to this section")
    return text.replace("with a number and a date", "with a figure and a page cite (dates are not checked in the lite version)")


def run(answers_text, issue_map, issues_meta, generate, control=None):
    """The whole lite hearing. issues_meta: {"I3": {"name":..., "section": "S1" or None}}."""
    control = control if control is not None else issue_map.get("control", [])
    rows = parse_answers(answers_text, control)
    by_n = {r["n"]: r for r in rows}
    asked = [r for r in rows if r["state"] != "control"]
    counts = {"asked": len(asked), "answered": sum(r["state"] == "answered" for r in asked),
              "refused": sum(r["state"] == "refused" for r in asked),
              "control_refused": sum(r["state"] == "control" for r in rows)}

    issues, section_states, section_decisive, judged = {}, {}, {}, {}
    for iid, spec in issue_map["issues"].items():
        meta = issues_meta[iid]
        qrows = [by_n[n] for n in spec["questions"] if n in by_n]
        qs = {}
        for r in qrows:
            qs[r["n"]] = {**r, "state": "answered" if r["state"] == "answered" else "no data", "check": (
                "figure checked on the cited page by the VPS run" if r["state"] == "answered" else "refused: " + r["reason"])}
        answered = [r for r in qrows if r["state"] == "answered"]
        state = "no data" if not answered else ("answered" if len(answered) == len(qrows) else "partial")
        rec = {"name": meta["name"], "section": meta.get("section"), "state": state, "questions": qs,
               "notes": [], "dropped": 0, "judge_score": None, "raw": [], "rejected": []}
        if answered:
            j = judge_issue(iid, meta["name"], qrows, generate)
            rec.update(notes=j["notes"], dropped=j["dropped"], judge_score=j["score"], raw=j["raw"], rejected=j["rejected"])
            if meta.get("section") and j["score"] is not None:
                judged[meta["section"]] = min(judged.get(meta["section"], 3), j["score"])
        issues[iid] = rec
        sec = meta.get("section")
        if sec:
            section_states.setdefault(sec, {}).update({"Q%d" % n: q["state"] for n, q in qs.items()})
            if spec.get("decisive"):
                section_decisive.setdefault(sec, []).append("Q%d" % spec["decisive"])

    ceilings = {s: rules.section_ceiling(section_states.get(s, {}), section_decisive.get(s, ["none"])) for s in rules.SECTIONS}
    judge_scores = {s: judged.get(s, ceilings[s][0]) for s in rules.SECTIONS}   # not judged = no lowering
    sections = rules.cap_scores(judge_scores, ceilings)
    for r in sections:   # court_rules wording was written for the full hearing; say what the lite evidence really is
        r["ceiling_why"] = _lite_why(r["ceiling_why"])
        r["cut"] = _lite_why(r["cut"]) if r["cut"] else r["cut"]
    for r in sections:
        r["judged"] = r["section"] in judged
    total = rules.trust_total(sections)
    key, reasons = rules.compute_position(total, [], False, True)
    return {"counts": counts, "issues": issues, "sections": sections, "total": total, "band": rules.band_of(total),
            "position_key": key, "position": rules.POSITION_LABEL[key], "position_reasons": reasons}


# ---------------------------------------------------------------- pages

def _css():
    mod = _load("build_stakeholder_page")
    return mod.CSS


def _e(s):
    return html.escape(str(s), quote=True)


def _page(title, body):
    return ("<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            "<title>%s</title><style>%s .wrap table{width:100%%;border-collapse:collapse} .wrap td,.wrap th{border-bottom:1px solid var(--line);"
            "padding:6px 8px;text-align:left;vertical-align:top;font-size:.9rem}</style></head><body><div class=\"wrap\">%s</div></body></html>"
            % (_e(title), _css(), body))


NOT_COMPARABLE = ("This is the LITE courtroom. It is not comparable to the full BIOCON hearing (trust 5 of 21, Wait): "
                  "different evidence (data-point answers from the annual report, decks and calls, each code-checked on its cited page), "
                  "fixed questions with no model-written lawyer, and no gates.")


def render_report(res, company):
    c = res["counts"]
    secs = "".join("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
        r["section"], _e(r["name"]), "n/a" if not r["judged"] else r["judge"], r["ceiling"], r["final"],
        _e(r["cut"] or r["ceiling_why"])) for r in res["sections"])
    iss = ""
    for iid, i in res["issues"].items():
        notes = "".join("<li>%s <em>Quote: &ldquo;%s&rdquo;</em></li>" % (_e(n["note"]), _e(n["quote"])) for n in i["notes"])
        dropped = " (%d note(s) dropped: quote not found in the answers)" % i["dropped"] if i["dropped"] else ""
        n_ans = sum(q["state"] == "answered" for q in i["questions"].values())
        iss += "<div class=\"row\"><h3>%s %s</h3><p>State: <b>%s</b> (%d of %d questions answered)%s</p>%s</div>" % (
            iid, _e(i["name"]), i["state"], n_ans, len(i["questions"]), dropped, "<ul>%s</ul>" % notes if notes else "")
    body = ("<h1>%s: lite courtroom</h1><p class=\"banner\"><b>%s</b></p>"
            "<p class=\"sub\">Questions asked: %d. Answered (figure and page cite): %d. Refused (no data): %d. "
            "The FIFA control question stayed refused and is not counted.</p>"
            "<h2>Trust</h2><div class=\"total\"><div><b>%d of 21</b>Trust (%s)</div><div><b>%s</b>Position</div></div>"
            "<p class=\"sub\">Band: %s (%s). %s. Judge column: n/a = the section had no judge score, so nothing was lowered. "
            "Ceilings and the position come from court_rules.py by code; the judge can only lower a score.</p>"
            "<table><tr><th>Section</th><th>Name</th><th>Judge</th><th>Ceiling</th><th>Final</th><th>Why</th></tr>%s</table>"
            "<p class=\"banner\">Gates were not checked in the lite version (pledge, auditor, order and similar findings). "
            "A real Buy needs them. Answered does not mean good: the score only shows that a figure was found on a cited page. No current price was read, so the position cannot be Buy.</p>"
            "<p class=\"sub\">Position reasoning: %s</p><h2>Issues</h2>%s"
            "<p class=\"sub\">Every figure is on the <a href=\"lite-receipts.html\">Receipts page</a>.</p>") % (
        _e(company), _e(NOT_COMPARABLE), c["asked"], c["answered"], c["refused"], res["total"], _e(res["band"]["meaning"]),
        _e(res["position"]), _e(res["band"]["range"]), _e(res["band"]["meaning"]), _e(res["band"]["caveat"]), secs,
        _e("; ".join(res["position_reasons"])), iss)
    return _page(company + " lite courtroom", body)


def render_receipts(res, company):
    out = ""
    for iid, i in res["issues"].items():
        if not i["questions"]:
            out += "<div class=\"row\"><h3>%s %s</h3><p class=\"nask\">no data: no question was asked for this issue.</p></div>" % (iid, _e(i["name"]))
            continue
        rows = "".join("<tr><td>%d</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
            q["n"], _e(q["question"]), _e(q["figure"]) if q["state"] == "answered" else "<span class=\"nask\">refused</span>",
            _e(q["source"]), _e(q["cite"]), _e(q["check"])) for q in i["questions"].values())
        out += ("<div class=\"row\"><h3>%s %s <small>(%s)</small></h3><table><tr><th>#</th><th>Question</th><th>Figure</th>"
                "<th>Source</th><th>Page</th><th>Code check</th></tr>%s</table></div>") % (iid, _e(i["name"]), i["state"], rows)
    body = ("<h1>%s: receipts</h1><p class=\"banner\">%s</p><p class=\"sub\">The code check was done by the VPS run "
            "(a figure must appear on the cited page); it is not re-run here. Only answered rows count as evidence. "
            "The FIFA control question is refused and left out.</p>%s") % (_e(company), _e(NOT_COMPARABLE), out)
    return _page(company + " receipts", body)


# ---------------------------------------------------------------- command line

def nemotron_generate(prompt):
    import nvidia_client
    res = nvidia_client.chat(MODEL, prompt, max_tokens=4000)
    if res["error"]:
        raise RuntimeError("Nemotron call failed: " + res["error"])
    return res["text"]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--answers", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--company", default="PI Industries (PIIND)")
    ap.add_argument("--map", default=str(REFS / "lite-issues.json"))
    ap.add_argument("--judge", choices=["auto", "nemotron", "none"], default="auto",
                    help="auto = Nemotron when NVIDIA_API_KEY is set, else no judge notes (offline)")
    a = ap.parse_args(argv)
    sys.path.insert(0, str(HERE))
    mode = a.judge
    if mode == "auto":
        mode = "nemotron" if os.environ.get("NVIDIA_API_KEY") else "none"
    if mode == "nemotron" and not os.environ.get("NVIDIA_API_KEY"):
        print("NVIDIA_API_KEY is not set (it only exists on the VPS).", file=sys.stderr)
        return 2
    generate = nemotron_generate if mode == "nemotron" else (lambda p: "")
    meta = {i["id"]: i for i in json.loads((REFS / "issues.json").read_text(encoding="utf-8"))["issues"]}
    imap = json.loads(Path(a.map).read_text(encoding="utf-8"))
    res = run(Path(a.answers).read_text(encoding="utf-8"), imap, meta, generate)
    res["judge_mode"] = mode
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "lite-report.html").write_text(render_report(res, a.company), encoding="utf-8")
    (out / "lite-receipts.html").write_text(render_receipts(res, a.company), encoding="utf-8")
    (out / "lite-result.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    print("judge: %s | trust %d of 21 | position %s | answered %d of %d" % (
        mode, res["total"], res["position"], res["counts"]["answered"], res["counts"]["asked"]))
    print("wrote", out / "lite-report.html", out / "lite-receipts.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
