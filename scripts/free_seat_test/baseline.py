"""Read the EXISTING Biocon brain (read-only) and list every quote it holds, with source id and speaker where given."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
BRAIN = ROOT.parent.parent / ".claude/skills/roast-room/brains/biocon-management"
Q = re.compile(r'"([^"]{20,400}?)"\s*\((S\d{3})(?:,\s*([^)]*?))?\)')
rows = []
for f in sorted(BRAIN.glob("*.md")):
    for m in Q.finditer(f.read_text(encoding="utf8")):
        meta = m.group(3) or ""
        speaker = re.split(r",| held|;", meta)[0].strip() if meta and not meta.strip().startswith(("deck", "held", "PDF")) else ""
        rows.append({"file": f.name, "sid": m.group(2), "speaker": speaker, "quote": m.group(1)})
(ROOT / "baseline-quotes.json").write_text(json.dumps(rows, ensure_ascii=False, indent=0))
uniq = {(r["sid"], r["quote"]) for r in rows}
print(len(rows), "quote mentions;", len(uniq), "distinct (sid, quote)")
import collections
print(collections.Counter(r["file"] for r in rows))
