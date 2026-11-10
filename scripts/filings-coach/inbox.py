"""Turn files dropped in build/filings-coach/inbox/ into readable page files.

Each file needs a short sidecar saying where it came from and why it is legal to use, because the
framework only uses sources it can stand behind. For inbox/my-book.pdf write inbox/my-book.json:
    {"title": "...", "author": "...", "year": "...", "url": "...",
     "legal_basis": "I own this copy" | "public domain" | "free from the author's site" | ...}

PDFs go through media_core.pdf_text (the one sanctioned PDF reader, which OCRs scanned pages);
.txt and .md files are copied as one page. Each document becomes books/md/<id>/p001.txt ...,
gets a manifest line, and the file moves to inbox/done/.

    python3 inbox.py
Then: python3 registry.py plan   (the new documents show up as "new")
"""
import json
import os
import re
import shutil
import subprocess
import sys

from paths import BOOKS_MD, BOOKS_RAW, INBOX, MANIFEST, TOOLKIT_SRC

TESSDATA = "/usr/share/tesseract-ocr/5/tessdata"   # local OCR language data (apt: tesseract-ocr-eng)


def make_id(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")[:60]


def pdf_to_pages(pdf, out_dir):
    env = dict(os.environ, PYTHONPATH=str(TOOLKIT_SRC))
    if os.path.isdir(TESSDATA):
        env["TESSDATA_PREFIX"] = TESSDATA
    done = subprocess.run([sys.executable, "-P", "-m", "media_core.pdf_text", str(pdf), "--out", str(out_dir)],
                          env=env, capture_output=True, text=True)
    if done.returncode != 0:
        raise RuntimeError(done.stderr.strip()[-300:])


def main():
    INBOX.mkdir(parents=True, exist_ok=True)
    (INBOX / "done").mkdir(exist_ok=True)
    added = 0
    for path in sorted(INBOX.iterdir()):
        if path.is_dir() or path.suffix == ".json":
            continue
        sidecar = path.with_suffix(".json")
        if not sidecar.exists():
            print(f"skip {path.name}: add {sidecar.name} with title, url and legal_basis first")
            continue
        meta = json.loads(sidecar.read_text())
        if not meta.get("legal_basis"):
            print(f"skip {path.name}: its sidecar has no legal_basis")
            continue
        doc_id = make_id(meta.get("id") or path.stem)
        out_dir = BOOKS_MD / doc_id
        if out_dir.exists() and any(out_dir.iterdir()):
            # Never overwrite a document that is already in the corpus: give it a new "id" in the sidecar.
            print(f"skip {path.name}: a document with id '{doc_id}' already exists; set a different \"id\" in {sidecar.name}")
            continue
        out_dir.mkdir(parents=True, exist_ok=True)
        BOOKS_RAW.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, BOOKS_RAW / f"{doc_id}{path.suffix}")
        try:
            if path.suffix.lower() == ".pdf":
                pdf_to_pages(path, out_dir)
            else:
                (out_dir / "p001.txt").write_text(path.read_text(errors="replace"))
            status = "ok"
        except RuntimeError as err:
            status = f"unreadable: {err}"
        pages = sorted(out_dir.glob("p*.txt"))
        row = {"id": doc_id, **meta, "pages": len(pages),
               "chars": sum(p.stat().st_size for p in pages), "status": status, "added_via": "inbox"}
        with MANIFEST.open("a") as f:
            f.write(json.dumps(row) + "\n")
        shutil.move(str(path), INBOX / "done" / path.name)
        shutil.move(str(sidecar), INBOX / "done" / sidecar.name)
        print(f"{doc_id}: {status}, {len(pages)} pages")
        added += 1
    print(f"added {added} document(s)")


if __name__ == "__main__":
    main()
