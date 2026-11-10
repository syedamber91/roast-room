# Filings-reading coach: the pipeline

This folder rebuilds and grows the leveled framework in `docs/filings-coach/` from two kinds of source:
SOIC course notes (in the sibling `learning-vault-invest` repo) and free, legal books and documents
(downloaded into `build/filings-coach/books/`, which is gitignored). Decisions behind it:
`docs/filings-coach/DECISIONS.md`.

Nothing here changes the framework by itself. New material always ends as a **proposed change** that the
owner approves.

## Files

| File | What it does |
|---|---|
| `paths.py` | Every path in one place (override with `FC_BUILD`, `FC_SOIC`, `FC_TOOLKIT`). |
| `inbox.py` | Turns files dropped in `build/filings-coach/inbox/` into page files plus a manifest line. Each file needs a sidecar `.json` with title, url and `legal_basis`. |
| `registry.py` | Fingerprints every source. `status` shows new / changed / removed; `plan` writes reading batches for only those; `record` stores fingerprints after reading. |
| `SCHEMA.md` | The extraction format every reader agent follows (one JSON line per check). |
| `verify.py` | Checks every extracted line mechanically: SOIC timestamps against the note, book quotes word for word against the page. Failed lines are never used. |
| `merge.py` | Puts verified checks in one file, tags their tier (soic / book / us-guide / classic), writes per-level files. |
| `BRIEF.md` | The brief for the Opus drafters that write framework levels from the merged checks. |
| `test_pipeline.py` | Tests for quote and cite verification and change detection: `python3 -m unittest test_pipeline -v`. |
| `propose.py` + `PROPOSE.md` | After new sources are read: lists checks no step cites yet and support that was retired, then briefs a Sonnet router and an Opus reviewer to write `docs/filings-coach/proposals/<date>.md`. |

## Adding new sources (the normal loop)

1. Drop a file and its sidecar `.json` in `build/filings-coach/inbox/`, then `python3 inbox.py`.
   (New SOIC notes need no step here: they appear in the vault and `registry.py` sees them.)
2. `python3 registry.py plan` writes `build/filings-coach/pending/soic-N.txt` and `book-N.txt`.
3. Reader agents (Sonnet for core material, Haiku for long or low-priority text) read each pending batch
   with `SCHEMA.md` and write `extract/<batch>.jsonl` (SOIC) or `extract/books/<batch>.jsonl` (books).
   Give each agent its own scratch folder: two agents sharing one once overwrote each other's helper script.
4. `python3 verify.py`, then `python3 merge.py`.
5. `python3 propose.py`, then the router and review in `PROPOSE.md`. The owner reads the proposal.
6. Only after approval: apply the edits to `docs/filings-coach/framework.md` and `framework-map.json`,
   add a dated changelog entry with the new version, and `python3 registry.py record`.

## Rules the pipeline keeps

- Numbers only when a source states them; `soic-ladder/rulebook/soic-ladder-rules-v1.yaml` wins on overlap.
- SOIC text is licensed: paraphrase only, never quoted. Book quotes are at most 25 words and only for verification.
- Classics (pre-1931) are support only; a reader's own inference (`merge/inference-ids.json`) is never support.
- No buy, sell or hold language. The coach says what to check, not what to do.
- PDFs are read only through `knowledge-toolkit`'s `media_core.pdf_text`. Scanned pages need local
  tesseract data (`apt-get install tesseract-ocr-eng`, then `TESSDATA_PREFIX`), because downloading it
  from GitHub is blocked by the network proxy.
- Run these scripts with plain `python3` (they import each other); use `python3 -I` only for one-off code
  that reads downloaded files.
