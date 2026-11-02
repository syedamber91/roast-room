#!/usr/bin/env python3
"""Add a "How the SOIC lawyer asked" panel to a built report.html.

    python add_method_panel.py <session>

Reads <session>/hearing.md and writes the panel just before the Exhibits section of <session>/report.html (and reader-card.html is left alone).
For every lawyer question it shows the issue, the question, and the SOIC source id and check named in WHY I ASK, so a reader can see
the lawyer worked from its own brain. Everything is counted from the hearing: nothing is typed in by hand.
"""
import html
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_hearing as chk  # noqa: E402

CSS = """<style>
#method .qrow{display:grid;grid-template-columns:5.5rem 1fr;gap:6px 14px;padding:10px 0;border-top:1px solid var(--line)}
#method .qrow:first-of-type{border-top:0}
#method .qid{font-family:var(--f-mono,monospace);font-size:.85rem;color:var(--muted)}
#method .qq{font-size:.95rem}
#method .why{grid-column:2;font-size:.85rem;color:var(--muted)}
#method .src{display:inline-block;background:var(--accent-soft);border-radius:4px;padding:0 6px;margin-right:4px;font-family:var(--f-mono,monospace);font-size:.8rem;color:var(--ink)}
#method .stats{display:flex;flex-wrap:wrap;gap:10px 28px;margin:8px 0 14px}
#method .stat b{font-size:1.4rem;font-family:var(--f-display,serif);display:block}
#method details{border-top:1px solid var(--line);padding:8px 0}
#method summary{cursor:pointer;font-weight:600}
</style>"""


def rows_of(hearing: str) -> list:
    out = []
    for t in chk.parse_turns(hearing):
        if t["role"] == "Lawyer" and re.match(r"^(Q|X)\d+ ", t["id"]):
            f = chk.fields(t["body"])
            issue = re.match(r"(I\d+|Cross)", t["section"])
            out.append({"issue": t["section"], "key": issue.group(1) if issue else "", "turn": t["id"].split()[0], "q": f.get("QUESTION", ""), "why": f.get("WHY I ASK", "")})
    return out


def panel(rows: list) -> str:
    ids = Counter(i for r in rows for i in set(re.findall(r"\bS\d{3}\b", r["why"])))
    per_issue = Counter(r["key"] for r in rows if r["key"].startswith("I"))
    asked = sum(per_issue.values())
    stats = [("%d" % asked, "questions in the ten issues"), ("%d" % len(per_issue), "issues heard"), (("%d on every issue" % min(per_issue.values())) if min(per_issue.values()) == max(per_issue.values()) else "%d to %d" % (min(per_issue.values()), max(per_issue.values())), "questions per issue"),
             ("%d" % len(ids), "different SOIC source ids cited"), ("%d" % len(rows), "lawyer turns incl. cross-examination")]
    top = ", ".join("%s (%d)" % (i, n) for i, n in ids.most_common(6))
    even = min(per_issue.values()) == max(per_issue.values())
    note = (" In this run it asked %d on every issue: its own rule allowed an early stop only once the decisive question was answered, and on no issue was it, so the freedom to ask fewer or more was not used." % min(per_issue.values())) if even else ""
    body = ['<section id="method"><div class="sec-head"><h2>How the SOIC lawyer asked</h2><p>Every question names the course source and check it came from. The lawyer could stop an issue at 2 to 5 questions.' + html.escape(note) + '</p></div><div class="card">',
            '<div class="stats">' + "".join('<div class="stat"><b>%s</b>%s</div>' % (html.escape(a), html.escape(b)) for a, b in stats) + "</div>",
            "<p class=\"look\">Most-cited sources: %s.</p>" % html.escape(top)]
    current = None
    for r in rows:
        if r["issue"] != current:
            if current is not None:
                body.append("</details>")
            current = r["issue"]
            body.append("<details><summary>%s</summary>" % html.escape(current))
        why = html.escape(r["why"])
        why = re.sub(r"\b(S\d{3})\b", r'<span class="src">\1</span>', why)
        body.append('<div class="qrow"><div class="qid">%s</div><div class="qq">%s</div><div class="why">%s</div></div>' % (html.escape(r["turn"]), html.escape(r["q"]), why))
    body.append("</details></div></section>")
    return CSS + "".join(body)


def main(session: Path) -> None:
    rows = rows_of((session / "hearing.md").read_text(encoding="utf-8"))
    page_path = session / "report.html"
    page = page_path.read_text(encoding="utf-8")
    if 'id="method"' in page:
        return
    page = page.replace('<section id="exhibits"', panel(rows) + '<section id="exhibits"', 1)
    page = page.replace('<a href="#exhibits">Exhibits</a>', '<a href="#method">Lawyer\'s method</a><a href="#exhibits">Exhibits</a>', 1)
    page = page.replace("<title>Courtroom Case Page</title>", "<title>Courtroom: BIOCON, SOIC analyst as lawyer</title>", 1)
    page_path.write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
