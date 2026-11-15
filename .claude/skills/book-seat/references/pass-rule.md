# Default pass rule (T4 reconciliation)

Owner decision 2026-11-15, from the Intelligent Investor run. A book's DECISIONS.md may override any line at T0; a
change made during a run is recorded there with its date and reason.

PASS only when all hold:

1. **Takeaways.** Every content section (author not "other", not a notes section) has at least one takeaway.
2. **Pages.** Every page has an item or a recorded reason. Code gives blank pages, notes sections and front or back
   matter their reason. Other pages get up to three looks by the extractor; after the third, a page still without an
   item that passes the quote check gets the reason "no item passed the quote check after 3 looks".
3. **Limit sentences.** Code flags a sentence that holds a directive word (should, must, require, limit...) AND a limit
   word (at least, no more than, below...) AND a number (years excluded; numbers that are names, such as 401(k),
   S&P 500, Fortune 500, Dow 30, ignored). It is covered when at least one of its numbers is in the threshold of a rule
   item on the page or the next one. Otherwise the extractor is asked for that rule, twice; an explicit empty answer
   ("not a limit") settles the page; what is still open is listed by page and number as a residual the owner accepts
   (`--accept-limit-residual`).
4. **Independent score.** After the fill step (the second reader reads every content page and its verified finds
   become items), an independent scorer reads a fresh seeded 10% sample. A miss counts when its quote is word for word
   on the page and overlaps no item already on that page or the next. Only rule and method misses are scored; the bar
   is under 10% of sampled pages. Other kinds are logged, not scored. The score is taken before scored misses are
   adopted as items; a later score needs a new seed.
5. **Calls.** Any failed model call (timeout, empty reply) blocks PASS and is retried on the next run. A failed call is
   never counted as a clean page.
