---
name: book-seat
description: Use when someone wants a Roast Room council seat built from a book they own, says "/book-seat", "make a seat from this book", "turn [book] into a council member", or wants a book's frameworks, rules and checks extracted with nothing important missed. Runs the whole pipeline the Intelligent Investor seat was built with - convert and OCR on the VPS, extract with free NVIDIA models, check every quote word for word in code, reconcile until a pass rule holds, store the full items in roast-room-private, write the public brain from verified items only, register the seat, optionally test it on companies, and hand off. Books only (v1). Not for people built from public work (that is /newroaster).
---

# /book-seat: a council seat from a book

One book in, one method seat out, built the same way as `intelligent` (The Intelligent Investor). The free models
propose; code decides. Claude never reads the book for retrieval: it writes the public brain only from items that
code has already checked word for word against the page.

Read before the first run: `references/lessons.md` (what broke last time and why), `references/pass-rule.md`,
`references/models.md`, `references/layout.md`, `references/vps-jobs.md`. Templates for the per-book files are in
`templates/`.

## Hard rules

- The book is the owner's own copy. Book text never enters roast-room or soic-ladder except short quotes (under 45
  words) in the public brain, each checked by `check_book_seat.mjs`. Full items live only in roast-room-private.
- Results PRs in soic-ladder carry counts and pages only (test-enforced). Close any that carries quotes.
- Never buy, sell or hold. A seat built from an investing book gives the book's tests, not picks.
- Every threshold the seat states comes from a verified rule item, with its id and page. None from memory.
- Author labels matter: keep each author's words apart (Graham vs Zweig taught this). A footnote filed under the wrong
  author is a known trap; flag, never quote it as the other author.
- Stop at the stop points below. Everything else runs without asking.

## Tasks

| Task | What | Who | Done when |
|---|---|---|---|
| T0 | Grill the owner with `references/t0-questions.md`; write DECISIONS.md and PLAN.md from `templates/` into roast-room-private `<seat_slug>/`; write soic-ladder `scripts/book_seat/books/<slug>/seat.json` | owner + Claude | owner confirms (stop point 1) |
| T1 | Book onto the VPS (owner copies it to `~/soic/books/`), convert, OCR for image pages | VPS `books-graph` (`check`, `run`, `ocr:<slug>`) | every page has text or is named as image-only |
| T2 | Section map: the heading detector, or a hand-made `books/<slug>/structure.json` (id, title, author, start, end) | VPS `structure:<slug>` | every page in exactly one section; owner approves (stop point 2) |
| T3 | Extract: Nemotron reads 2-page windows; the gate keeps an item only if its quote is word for word on the page | VPS `seat-extract:<slug>` (smoke first: `seat-extract-smoke:<slug>`) | failed calls 0 (re-run; replies are cached) |
| T4 | Reconcile to the pass rule (`references/pass-rule.md`) | VPS `seat-reconcile:<slug>` | RECONCILIATION.md says PASS |
| T5 | Private store into roast-room-private `<seat_slug>/` | VPS `seat-private:<slug>` | README index, sections, kind files, items_final.jsonl pushed |
| T6 | Public brain in roast-room `brains/<seat_slug>/` from verified items, by three writer agents (`templates/writer-briefs.md`), then `_hot.md` by Claude | Claude | `check_book_seat.mjs` passes, 0 unchecked quoted runs |
| T7 | Agent `.claude/agents/council-<key>.md` (model: `council-intelligent.md`), `add_seat.mjs` (on call unless owner says default), tension lines in `references/seats.md`, test consult | Claude | consult quotes pass the checker; seat refuses buy/sell/hold |
| T8 | Company test, investing books only: PREREG.md first (`templates/PREREG.md`), `books/<slug>/tests.json` from verified rule items, then score | owner approves PREREG (stop point 5), VPS `seat-companies:<slug>` | pass rule in PREREG section 7 holds; results recorded as they are |
| T9 | Handoff: `templates/HANDOFF.md` into roast-room-private and soic-ladder `docs/` | Claude | both pushed |

Non-investing books skip T8 (or the owner names a test decision at T0).

## Stop points (ask the owner, then wait)

1. End of T0: seat key, name, question, authors, T8 or not, any pass-rule or model change.
2. End of T2: the section map.
3. Before more than 1,000 model calls in one step, and before any re-extraction after a failed check.
4. A failed check whose fix would change a bar or a rule. Code-only fixes (bugs, retries, gate fixes) go ahead and
   are reported.
5. Before T8 scores: PREREG approval. Nothing in it is tuned afterwards.
6. New keys or new fetches (deploy key, public material, extra documents).

## Checking the work

- `node .claude/skills/newroaster/scripts/check_book_seat.mjs .claude/skills/roast-room/brains/<seat_slug> <roast-room-private>/<seat_slug>/items_final.jsonl`
  before every commit of the public brain. It needs roast-room-private cloned beside roast-room.
- soic-ladder tests: `PYTHONPATH=src:scripts python3 -m pytest tests/test_book_seat_*.py tests/test_soic_run.py -k "book_seat or books_graph"`.
- A VPS run is read from its live log (`live-logs/<date>-books-graph-<run>-1`, files STATUS.md and tail.log) and its
  results branch (`results/books-graph-<date>-<time>`).

## Report at the end

Seat key and question; items kept; the pass-rule result with numbers; public brain files and checker counts; T8
prediction against result if run; open items. Plain English, no em dashes.
