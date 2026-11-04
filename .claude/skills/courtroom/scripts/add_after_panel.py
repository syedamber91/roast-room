#!/usr/bin/env python3
"""Add an "After the hearing" section to a built report.html.

    python add_after_panel.py <session>

Reads <session>/after-hearing.json (a list of {flag, topic, text, source}) and writes one section just before the Exhibits section.
These are facts found AFTER the court sat. They were not put to the Convict, so they change no answer state, no judge score and no
trust total. Idempotent: a page that already has the section is left alone.
"""
import html
import json
import sys
from pathlib import Path

CSS = """<style>
#after .arow{padding:10px 0;border-top:1px solid var(--line)}
#after .arow:first-of-type{border-top:0}
#after .aflag{font-family:var(--f-mono,monospace);font-size:.85rem;color:var(--muted)}
#after .asrc{font-size:.85rem;color:var(--muted)}
</style>"""


def panel(items: list) -> str:
    rows = "".join('<div class="arow"><b>%s</b> <span class="aflag">(red flag %s)</span><div>%s</div><div class="asrc">Source: %s</div></div>'
                   % (html.escape(i["topic"]), html.escape(i["flag"]), html.escape(i["text"]), html.escape(i["source"])) for i in items)
    return (CSS + '<section id="after"><div class="sec-head"><h2>Found after the hearing</h2><p>These were read from the filings after the court sat. '
            'They were not put to the Convict, so they change no answer state, no judge score and no trust total. Read them beside the matching red flag.</p></div>'
            '<div class="card">' + rows + '</div></section>')


def main(session: Path) -> None:
    items = json.loads((session / "after-hearing.json").read_text(encoding="utf-8"))
    path = session / "report.html"
    page = path.read_text(encoding="utf-8")
    if 'id="after"' in page:
        return
    page = page.replace('<section id="exhibits"', panel(items) + '<section id="exhibits"', 1)
    page = page.replace('<a href="#exhibits">Exhibits</a>', '<a href="#after">After the hearing</a><a href="#exhibits">Exhibits</a>', 1)
    path.write_text(page, encoding="utf-8")


if __name__ == "__main__":
    main(Path(sys.argv[1]))
