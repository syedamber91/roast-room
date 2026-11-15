# VPS jobs (soic-ladder workflow soic-run.yml, job books-graph, input `companies` = the mode)

Dispatch on branch `claude/jolly-hopper-jqj20i` (a new mode needs nothing on main; a new job name would). One run at a
time per artifacts group; two runs finishing in the same minute collide on the results branch name, so wait for one
before the next. Each step is capped at 60 minutes; every model reply is cached, so re-dispatch to continue.

| Mode | Step | Writes |
|---|---|---|
| `check` / `run` / `ocr:<slug>` | T1 convert and OCR | `books-out/converted/<slug>/p001.txt...` |
| `structure:<slug>` | T2 section map (uses `books/<slug>/structure.json` when present) | results PR: structure report |
| `seat-extract-smoke:<slug>` then `seat-extract:<slug>` | T3 | `books-out/seat/<slug>/items.jsonl`; results PR: counts |
| `seat-reconcile:<slug>` | T4 (fill, scorer, number-rule asks, third look) | `seat/<slug>/reconcile/`; results PR: RECONCILIATION.md, ledger, diagnostics (titles only) |
| `seat-private:<slug>` | T5 | roast-room-private `<seat_slug>/` |
| `seat-companies:<slug>` | T8 | roast-room-private `<seat_slug>/company-test/`; results PR: counts |

Read progress from the live-log branch: `git show origin/live-logs/<date>-books-graph-<run>-1:tail.log`.
