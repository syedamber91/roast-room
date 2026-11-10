"""Where everything lives. Change a path here and every script follows.

The build folder is gitignored: downloaded books and extracted checks stay on this machine.
Only the scripts, the schema, the briefs, the manifest and the framework itself are committed.
"""
import os
from pathlib import Path

# The repo this file lives in: roast-room/scripts/filings-coach/paths.py -> roast-room/
REPO = Path(__file__).resolve().parents[2]

# Working folder for the pipeline (gitignored). Override with FC_BUILD if you keep it elsewhere.
BUILD = Path(os.environ.get("FC_BUILD", REPO / "build" / "filings-coach"))

# SOIC course notes (the learning-vault-invest repo). Override with FC_SOIC.
SOIC = Path(os.environ.get("FC_SOIC", REPO.parent / "learning-vault-invest" / "wiki" / "personas" / "soic"))

# The one sanctioned PDF reader lives in knowledge-toolkit (see its CLAUDE.md). Override with FC_TOOLKIT.
TOOLKIT_SRC = Path(os.environ.get("FC_TOOLKIT", REPO.parent / "knowledge-toolkit" / "src"))

BOOKS_MD = BUILD / "books" / "md"            # one folder per document, p001.txt, p002.txt ...
BOOKS_RAW = BUILD / "books" / "raw"          # the downloaded bytes
MANIFEST = BUILD / "books" / "manifest.jsonl"  # one line per document: url, legal basis, status
INBOX = BUILD / "inbox"                      # drop new sources here
EXTRACT = BUILD / "extract"                  # SOIC checks: extract/*.jsonl ; book checks: extract/books/*.jsonl
PENDING = BUILD / "pending"                  # batch lists for sources that still need reading
MERGE = BUILD / "merge"                      # merged checks and per-level files
REGISTRY = BUILD / "registry.json"           # fingerprint of every source already read

# Committed outputs.
DOCS = REPO / "docs" / "filings-coach"
FRAMEWORK_MAP = DOCS / "framework-map.json"  # stable step id -> the check ids that support it
