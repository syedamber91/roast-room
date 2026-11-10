"""Keep a fingerprint of every source, so a re-run reads only what is new or changed.

A "source" is either one SOIC note (a .md file) or one book/document (a folder of page files).
Its fingerprint is the sha256 of its text. If the text changes, the fingerprint changes, and the
source is read again. If a source disappears, its checks are flagged for retirement.

Commands:
    python3 registry.py status      # counts of new / changed / removed / unchanged sources
    python3 registry.py plan        # write reading batches for new and changed sources into pending/
    python3 registry.py record      # after reading + verify: store today's fingerprints as "read"
    python3 registry.py bootstrap   # first run only: mark everything read so far as read
"""
import hashlib
import json
import sys
from datetime import date

from paths import BOOKS_MD, MANIFEST, PENDING, REGISTRY, SOIC


def fingerprint_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fingerprint_folder(folder):
    # Hash the page files in name order, so p001 + p002 ... always gives the same answer.
    h = hashlib.sha256()
    for page in sorted(folder.glob("p*.txt")):
        h.update(page.name.encode())
        h.update(page.read_bytes())
    return h.hexdigest()


def readable_books():
    """Book ids the manifest marks as readable ('ok'). Stubs and failures are skipped."""
    books = {}
    for line in MANIFEST.read_text().splitlines():
        if line.strip():
            row = json.loads(line)
            if row.get("status") == "ok":
                books[row["id"]] = row
    return books


def scan_sources():
    """Return {source_id: {"kind": ..., "path": ..., "sha256": ...}} for everything on disk now."""
    found = {}
    for folder in ("concepts", "topics"):
        for note in sorted((SOIC / folder).glob("*.md")):
            found[note.stem] = {"kind": "soic", "path": str(note), "sha256": fingerprint_file(note)}
    for book_id in readable_books():
        folder = BOOKS_MD / book_id
        if folder.is_dir():
            found[book_id] = {"kind": "book", "path": str(folder), "sha256": fingerprint_folder(folder)}
    return found


def load_registry():
    return json.loads(REGISTRY.read_text()) if REGISTRY.exists() else {}


def compare(now, before):
    new = [s for s in now if s not in before]
    changed = [s for s in now if s in before and now[s]["sha256"] != before[s]["sha256"]]
    removed = [s for s in before if s not in now]
    unchanged = [s for s in now if s in before and now[s]["sha256"] == before[s]["sha256"]]
    return new, changed, removed, unchanged


def cmd_status():
    new, changed, removed, unchanged = compare(scan_sources(), load_registry())
    print(f"new {len(new)}  changed {len(changed)}  removed {len(removed)}  unchanged {len(unchanged)}")
    for label, ids in (("new", new), ("changed", changed), ("removed", removed)):
        for s in ids[:20]:
            print(f"  {label}: {s}")


def cmd_plan(batch_size=20):
    """Write pending/soic-N.txt and pending/book-N.txt: the sources a reader agent should read next."""
    now = scan_sources()
    new, changed, removed, _ = compare(now, load_registry())
    todo = new + changed
    PENDING.mkdir(parents=True, exist_ok=True)
    for old in PENDING.glob("*.txt"):
        old.unlink()
    for kind in ("soic", "book"):
        items = [s for s in todo if now[s]["kind"] == kind]
        for n in range(0, len(items), batch_size):
            batch = items[n:n + batch_size]
            # SOIC readers take note paths; book readers take document ids (same format as before).
            lines = [now[s]["path"] if kind == "soic" else s for s in batch]
            (PENDING / f"{kind}-{n // batch_size + 1}.txt").write_text("\n".join(lines) + "\n")
    (PENDING / "removed.json").write_text(json.dumps(removed, indent=1))
    print(f"planned {len(todo)} sources to read ({len(new)} new, {len(changed)} changed); "
          f"{len(removed)} removed (their checks will be retired). Batches in {PENDING}")


def cmd_record(only=None):
    """Store fingerprints as 'read'. `only` limits it to a set of source ids (default: all on disk)."""
    reg = load_registry()
    today = date.today().isoformat()
    for s, info in scan_sources().items():
        if only is None or s in only:
            reg[s] = {**info, "read_on": today}
    REGISTRY.write_text(json.dumps(reg, indent=1, sort_keys=True))
    print(f"registry now holds {len(reg)} sources")


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "status"
    if command == "status":
        cmd_status()
    elif command == "plan":
        cmd_plan()
    elif command in ("record", "bootstrap"):
        cmd_record()
    else:
        sys.exit(__doc__)
