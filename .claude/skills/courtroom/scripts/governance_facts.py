"""Board, executives and auditors, read from fixed annual report pages by code.

Every line carries its page id, written (AR p188). Nothing here is a judgment: names and
dates are copied as printed, counts are worked out from printed tables, and a thing that
the pages do not say is listed as not in the record. Nothing from a call or a deck.
"""

import os
import re
from pathlib import Path

DEFAULT_LADDER = Path(os.environ.get("SOIC_LADDER", "/home/user/soic-ladder"))


def page_text(ar_dir: Path, n: int) -> str:
    f = ar_dir / ("p%03d.md" % n)
    return f.read_text(encoding="utf-8") if f.exists() else ""


def clean(text: str) -> str:
    """Page text with markdown marks and soft line breaks removed, so a sentence reads as one line."""
    text = re.sub(r"<br>|<sup>|</sup>|\*\*|_{1,2}", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def corporate_info(text: str) -> dict:
    """{heading: text under it} for a corporate-information page whose headings look like '###### **Audit Committee**'."""
    parts = re.split(r"^#{4,6}\s+\*{0,2}(.+?)\*{0,2}\s*$", text, flags=re.M)
    return {parts[i].strip(): clean(parts[i + 1]) for i in range(1, len(parts) - 1, 2)}


def role_changes(info: dict) -> list:
    """(heading, text) for each heading whose text says someone was appointed, stepped down or ceased."""
    return [(h, t) for h, t in info.items() if re.search(r"Appointed w\.e\.f\.|Stepped down|Ceased", t)]


def attendance(text: str) -> tuple:
    """(meetings held or None, [(name, entitled, attended, percent)]) from a board-meeting page."""
    held = re.search(r"(\d+)\s*\(\w+\)\s*Board Meetings were held", text)
    rows = []
    for m in re.finditer(r"^\|([A-Za-z][^|]+)\|(\d+)\|(\d+)\|([\d.]+)\|(?:Yes|No)", text, re.M):
        rows.append((m.group(1).strip(), int(m.group(2)), int(m.group(3)), float(m.group(4))))
    return (int(held.group(1)) if held else None), rows


def kam_titles(text: str) -> list:
    """Key audit matter titles: bold first cells in an audit report table, before the 'See Note' line."""
    out = []
    for m in re.finditer(r"^\|\*\*([^|]+?)\*\*(?:<br>[^|]*)?\|\|$", text, re.M):
        title = re.sub(r"\s+", " ", m.group(1).split("<br>")[0]).strip(" *")
        if title and not title.lower().startswith(("see note", "the key audit matter", "how the matter")) and title not in out:
            out.append(title)
    return out


def sentences(paragraph: str) -> list:
    """Split at a full stop that follows a lower-case letter, digit or bracket and is followed by a word like 'Subsequently'.
    Names such as 'B S R & Co. LLP' and 'S. R. Batliboi' do not split, because the next word is all capitals or the letter before is one."""
    return [s.strip() for s in re.split(r"(?<=[a-z0-9)\u2019])\.\s+(?=[A-Z][a-z]+)", paragraph) if s.strip()]


def governance_block(ar_dir: Path, pages: dict) -> str:
    """The chapter 4 'Board and auditors' block as markdown. Missing pages give a plain not-in-the-record line."""
    if not ar_dir or not ar_dir.exists():
        return "### Board, executives and auditors\n\nNot in the record: the annual report pages were not available to this run.\n"
    lines = ["### Board, executives and auditors, from the annual report", "",
             "Names and dates are copied as printed. Counts are worked out by code from printed tables. The pdf page number is in brackets.", ""]
    ci, pg = corporate_info(page_text(ar_dir, pages["corporate_info"])), pages["corporate_info"]
    for heading in ("Executive Chairperson", "CEO and Managing Director", "Non-Executive, Non-Independent Directors", "Independent Directors"):
        if heading in ci:
            lines.append("- %s, as printed: %s (AR p%d)" % (heading, ci[heading], pg))
    lines += ["- Committees as printed: " + "; ".join("%s: %s" % (h, ci[h]) for h in ci if h.endswith("Committee")) + " (AR p%d)" % pg]
    changes = role_changes(ci)
    if changes:
        lines += ["", "Changes in roles during or just after the year, as printed:", ""]
        lines += ["- %s: %s (AR p%d)" % (h, t, pg) for h, t in changes]
    held, rows = attendance(page_text(ar_dir, pages["board_meetings"]))
    pb = pages["board_meetings"]
    if held and rows:
        low = min(rows, key=lambda r: r[3])
        lines += ["", "Board meetings and attendance:", "",
                  "- Meetings held in the year: %d (AR p%d)." % (held, pb),
                  "- Directors in the attendance table: %d. Lowest attendance: %s, %d of %d meetings, %.2f%% (AR p%d, derived)." % (len(rows), low[0], low[2], low[1], low[3], pb)]
    auditors = ci.get("Statutory Auditors", "")
    para = clean(re.search(r"Statutory Auditors\s*\n(.*?)(?:\n#{4,6}|\Z)", page_text(ar_dir, pages["auditors"]), re.S).group(1)) if re.search(r"Statutory Auditors\s*\n", page_text(ar_dir, pages["auditors"])) else ""
    if auditors or para:
        lines += ["", "Statutory auditors:", ""]
        if auditors:
            lines.append("- Named on the corporate information page: %s (AR p%d)." % (auditors.split(" Chartered")[0], pg))
        lines += ["- %s (AR p%d)" % (s, pages["auditors"]) for s in sentences(para)]
    kc = [t for n in pages.get("kam_consolidated", []) for t in kam_titles(page_text(ar_dir, n))]
    ks = [t for n in pages.get("kam_standalone", []) for t in kam_titles(page_text(ar_dir, n))]
    if kc or ks:
        lines += ["", "Key audit matters named by the auditor:", ""]
        if ks:
            lines.append("- Standalone report: %s (AR p%s)" % ("; ".join(ks), ", p".join(str(n) for n in pages["kam_standalone"])))
        if kc:
            lines.append("- Consolidated report: %s (AR p%s)" % ("; ".join(kc), ", p".join(str(n) for n in pages["kam_consolidated"])))
        pages_checked = pages.get("kam_standalone", []) + pages.get("kam_consolidated", [])
        has_emphasis = any(re.search(r"emphasis of matter", page_text(ar_dir, n), re.I) for n in pages_checked)
        lines.append("- The words 'Emphasis of Matter' %s on the audit report pages (AR p%s, derived by searching those pages)." % ("appear" if has_emphasis else "do not appear", ", p".join(str(n) for n in pages_checked)))
    lines += ["", "What this block does not hold: how long each independent director has served, any director's pay, the auditor's fees (annual report note 28), "
              "the skills table on AR p35, and anything about the incoming auditor beyond its name and term.", ""]
    return "\n".join(lines)
