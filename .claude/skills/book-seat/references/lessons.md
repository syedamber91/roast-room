# Lessons from the Intelligent Investor run (2026-11-14 to 15)

Each one cost a run. Read before T3.

- **Wrong page numbers are the commonest reject.** The gate relocates a quote to the page in its window where it really
  is, before rejecting it.
- **Models invent kind names** (teaching_example, named_idea, Warning). Map them (`KIND_ALIASES` in extract.py) and
  list the allowed kinds in every prompt.
- **Models paraphrase quotes.** Tell them code checks word for word and drops an item if one word differs; use 2-page
  windows and "every idea, up to 10".
- **A failed call must never count as a clean result.** It blocks PASS and is not cached, so the next run retries it.
- **Empty replies from a reasoning model** come from long thinking eating the token budget: "Reasoning: low" and more
  max_tokens fixed gpt-oss-20b.
- **Listed models can be retired** (404/410). The scorer falls through a list; it never switches on slowness.
- **Scoring with the model that filled is rigged.** The scorer must be a model that never extracted or filled.
- **A limit-sentence detector is noisy.** Require a directive AND a limit word; ignore years and name-numbers; accept
  an explicit "not a limit".
- **The 60-minute cap.** Cache every reply by a stable key, run calls in parallel (4 to 6 workers), print progress
  lines ("fill N/514", "reader N/51") so the live log shows movement.
- **An edit can silently miss its anchor.** After a Python string replace, grep that the new code is there; a passing
  test suite did not catch a missing third look.
- **Footnotes filed under the main author.** In the Intelligent Investor about 7 to 10 items in Graham chapters were
  Zweig's 2003 footnotes. Writers must flag dated wording ("in early 2003") and never quote it as the main author.
- **Quotes stay private.** items.jsonl, rejects and items_final never go into a results PR; the brain checker needs the
  private repo cloned.
- **Old numbers misfire.** A 1972 US price bar failed every good Indian company in 2026; say so in "where this lens
  misfires", and never tune a bar after the score.
