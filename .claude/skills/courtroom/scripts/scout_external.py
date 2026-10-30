#!/usr/bin/env python3
"""Fetch outside evidence for the external baseline questions and write external.md.

    python scout_external.py <session> --company BIOCON --queries queries.json --last30days
    python scout_external.py <session> --company BIOCON --results-json items.json

Two ways in, one way out. Items come either from the last30days skill (run as a command)
or from a JSON file the host gathered another way, for example with web search. Both go
through the same screen and the same writer:

- screen: an item with no date, a date outside the window (a rule or policy still in force carries `"standing": true` and skips only this one test), a repeated link, or text that
  tries to give instructions to a reader is dropped, and each drop is listed with its reason;
- ids: kept items get E001 and up, in question order;
- label: every item says it is context only and may never answer a question about the
  company's own numbers (check_hearing.py enforces that on the hearing).

If nothing survives for a question, external.md says so in plain words. It never fills a
question with a guess.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlparse

WINDOW_DAYS = 45          # an item older than this before the run date is stale
PER_QUESTION = 3          # at most this many items kept for one question
SNIPPET_CHARS = 280
MIN_RELEVANCE = 0.3       # last30days gives each result a score; below this it is chatter, not evidence
LAST30DAYS = Path(os.environ.get("LAST30DAYS_SCRIPT", "/home/user/knowledge-toolkit/.claude/skills/last30days/scripts/last30days.py"))

# Text that talks to a reader instead of describing the world. A page can plant these.
INJECTION_RE = re.compile(
    r"ignore (?:all |any |the )?(?:previous|prior|above)|disregard (?:the |all |any )?(?:previous|above|instructions)|system prompt|"
    r"you are (?:now|an?|the) (?:ai|assistant|model|judge|lawyer)|as an ai|begin (?:system )?prompt|<\s*script|"
    r"do not (?:tell|reveal)|new instructions|override (?:the )?(?:rules|score|position)|rate (?:this|it) (?:buy|sell)",
    re.I)


def parse_date(text) -> date | None:
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})", str(text or ""))
    try:
        return date(int(m.group(1)), int(m.group(2)), int(m.group(3))) if m else None
    except ValueError:
        return None


def screen(items: list, run_date: date) -> tuple:
    """Return (kept, dropped). dropped is a list of (item, reason). Order inside a question is kept."""
    kept, dropped, seen = [], [], set()
    for item in items:
        text = " ".join(str(item.get(k, "")) for k in ("title", "snippet"))
        when = parse_date(item.get("date"))
        url = str(item.get("url", "")).strip()
        if not url.startswith("http"):
            dropped.append((item, "no link"))
        elif when is None:
            dropped.append((item, "no date"))
        elif when > run_date:
            dropped.append((item, "dated after the run date"))
        elif run_date - when > timedelta(days=WINDOW_DAYS) and not item.get("standing"):
            dropped.append((item, "older than %d days" % WINDOW_DAYS))
        elif item.get("relevance") is not None and float(item["relevance"]) < MIN_RELEVANCE:
            dropped.append((item, "low relevance score"))
        elif url in seen:
            dropped.append((item, "repeated link"))
        elif INJECTION_RE.search(text):
            dropped.append((item, "text tries to instruct a reader (injection screen)"))
        elif not str(item.get("snippet", "")).strip():
            dropped.append((item, "no text"))
        else:
            seen.add(url)
            kept.append(item)
    return kept, dropped


def clean_snippet(text: str) -> str:
    text = re.sub(r"\s+", " ", str(text)).strip().replace('"', "'")
    return text if len(text) <= SNIPPET_CHARS else text[:SNIPPET_CHARS].rsplit(" ", 1)[0] + " ..."


def build_external(items: list, questions: list, company: str, run_date: date, method: str) -> tuple:
    """questions: [{"id": "B18", "question": "..."}]. Returns (external.md text, E-id map, dropped list)."""
    kept, dropped = screen(items, run_date)
    lines = ["# Outside evidence: %s" % company, "",
             "Fetched %s by %s. Context only: these items may describe the business picture and may feed a trigger, "
             "but they may never raise a score, lift the position, or answer a question about the company's own numbers. "
             "Each item passed a date check and an injection screen; every drop is listed at the end." % (run_date.isoformat(), method), ""]
    ids, n = {}, 0
    for q in questions:
        mine = [i for i in kept if i.get("question") == q["id"]][:PER_QUESTION]
        lines += ["## %s: %s" % (q["id"], q["question"]), ""]
        if not mine:
            lines += ["Nothing usable was fetched for this question. The record does not hold an outside view of it.", ""]
            continue
        for item in mine:
            n += 1
            eid = "E%03d" % n
            ids[eid] = item["url"]
            lines += ["### %s" % eid, "",
                      "- Question: %s" % q["id"],
                      "- Title: %s" % clean_snippet(item.get("title", "")),
                      "- Source: %s (%s)" % (urlparse(item["url"]).netloc, item["url"]),
                      "- Date: %s" % item["date"],
                      '- Text: "%s"' % clean_snippet(item["snippet"]),
                      "- Use: context only, never a company fact.", ""]
    lines += ["## Dropped by the screen", ""]
    lines += ["- %s | %s" % (clean_snippet(i.get("title") or i.get("url") or "item")[:80], why) for i, why in dropped] or ["- none"]
    return "\n".join(lines) + "\n", ids, dropped


def run_last30days(queries: list, run_date: date) -> list:
    """One last30days run per question query. Returns items in the common shape. An empty list is a real answer."""
    items = []
    env = dict(os.environ, LAST30DAYS_ALLOW_ENGINE_PLAN="1")
    for q in queries:
        try:
            out = subprocess.run([sys.executable, str(LAST30DAYS), "--research-only", "--quick", "--emit", "json", "--days", "30",
                                  "--as-of", run_date.isoformat(), "--web-backend", "keyless", q["query"]],
                                 capture_output=True, text=True, timeout=170, env=env).stdout
            data = json.loads(out)
        except (subprocess.SubprocessError, json.JSONDecodeError, OSError):
            continue
        for r in data.get("results", []):
            items.append({"question": q["id"], "title": r.get("title", ""), "url": r.get("url", ""),
                          "date": r.get("date") or r.get("published_at") or "", "snippet": r.get("snippet") or r.get("summary") or r.get("text") or "", "relevance": r.get("relevance_score")})
    return items


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("session", type=Path)
    ap.add_argument("--company", required=True)
    ap.add_argument("--run-date", default=date.today().isoformat())
    ap.add_argument("--queries", type=Path, help='JSON list of {"id": "B18", "question": "...", "query": "..."}')
    ap.add_argument("--last30days", action="store_true", help="run the last30days skill for each query")
    ap.add_argument("--results-json", type=Path, help="items gathered another way: a JSON list of {question, title, url, date, snippet}")
    a = ap.parse_args()
    run = date.fromisoformat(a.run_date)
    queries = json.loads(a.queries.read_text(encoding="utf-8")) if a.queries else []
    questions = [{"id": q["id"], "question": q["question"]} for q in queries]
    items, methods = [], []
    if a.results_json:
        items += json.loads(a.results_json.read_text(encoding="utf-8"))
        methods.append("web search gathered by the host")
        if not questions:
            questions = [{"id": q, "question": q} for q in sorted({i["question"] for i in items})]
    if a.last30days:
        items += run_last30days(queries, run)
        methods.append("the last30days skill")
    if not methods:
        raise SystemExit("give --last30days or --results-json (or both)")
    method = " and ".join(methods)
    text, ids, dropped = build_external(items, questions, a.company, run, method)
    (a.session / "external.md").write_text(text, encoding="utf-8")
    print("wrote external.md: %d kept, %d dropped, from %d items" % (len(ids), len(dropped), len(items)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
