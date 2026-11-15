# Where everything goes

| What | Where |
|---|---|
| Book file | VPS `~/soic/books/` (owner copies it; never in a repo) |
| Converted pages, OCR, extraction cache, items, reconcile cache | VPS `~/soic/books-out/` (`converted/<slug>/`, `seat/<slug>/`) |
| Per-book settings | soic-ladder `scripts/book_seat/books/<slug>/`: `seat.json` (seat_slug, seat_key, investing), optional `structure.json` (hand-made section map), optional `tests.json` (T8) |
| Decisions, plan, pre-registration, full store, company test, handoff | roast-room-private `<seat_slug>/` on branch `claude/jolly-hopper-jqj20i` |
| Public brain | roast-room `.claude/skills/roast-room/brains/<seat_slug>/` |
| Agent, roster, tensions | roast-room `.claude/agents/council-<key>.md`, `roster.json`, `references/seats.md` |
| Counts-only reports | soic-ladder `docs/reports/books-graph/seat/<slug>/` (results PRs) |

The VPS pushes to roast-room-private with the deploy key `~/.ssh/roast_room_private` ("soic-vps book-seat writer",
write access to that repo only). `<slug>` is the converted book's folder name; `<seat_slug>` comes from seat.json.
