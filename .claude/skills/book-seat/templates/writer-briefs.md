# T6 writer briefs (three agents in parallel, general-purpose)

Shared block for every brief (fill <...>):

> You are writing part of a Roast Room METHOD seat for the book <title> (<authors and their labels>). Read only:
> roast-room-private `<seat_slug>/sections/*.md` and the kind files (takeaways, methods, rules, frameworks, warnings,
> examples). Format examples: `brains/intelligent-investor/` and `brains/soic-analyst/`; spec:
> `.claude/skills/newroaster/references/brain-spec.md`.
> Use only what is in the items, nothing from memory; list well-known ideas the items lack under "Not found in the
> extracted items". Every quote is copied EXACTLY as a contiguous piece of one item's Quote field, under 45 words, in
> straight double quotes, followed by the section id in parentheses, then `[full: <item id>]`. Paraphrase never in
> quotation marks. Label every point with its author; show both when authors differ. Numbers carry their era and
> place. Plain English, no em dashes, never buy, sell or hold. Each file opens with "# <File>: <title>" and one line
> saying it was built from <N> verified items in the private store. When done, run check_book_seat.mjs on the folder
> and fix your files until clean. Edit only your files. Do not commit.

- **Writer 1 (rules side):** frameworks.md (15-25), principles.md (20-30, confidence by number of sections), rules.md
  (every numeric limit as printed, item id, page, era), checks.md (the book's checklists, then what the book does not
  test).
- **Writer 2 (chapters side):** chapters.md (per section: what each author says, tests, "use this when"; then the whole
  book in one framework of 6-10 steps), positions.md (25-35 common questions; "no recorded position" when the items are
  silent), books.md.
- **Writer 3 (voice side):** voice.md, stories.md, examples.md, warnings.md, and a commentary file when the book has a
  second author.

Claude then writes `_hot.md` (who the seat is, the question, worldview, eight rules with quotes, five frameworks, the
decision loop, signature questions, voice, where this lens misfires) and runs the checker on the whole folder.
