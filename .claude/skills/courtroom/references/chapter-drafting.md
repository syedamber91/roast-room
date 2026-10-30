# Drafting case book chapters 1, 2 and 7 (company terms)

A model drafts these from the annual report's business pages only. Code then checks every line (`scripts/check_chapters.py`). The case book builder uses the draft only when every check passes.

**Who reads it.** A 15-year-old with no background in markets. The judge learns the company from these chapters.

**Sources.** Only the page files named in `docs/company-record/<company>/ar-pages.json` under `business_pages`. Never a call, a deck, a news item or a brain. Never open anything under `.claude/skills/roast-room/brains/`.

**Output file.** `docs/company-record/<company>/chapters-1-2-7.md`, in exactly this shape:

```
## 1. The company in plain words
- One short sentence about what the company is or does. (AR p13)
## 2. How it makes money
- One short sentence about a business, a product line, a customer type or how it is paid. (AR p14)
## 7. Glossary
- Term: its plain meaning for this company. (AR p15)
```

**Rules, each checked by code.**
1. One sentence per line, at most 25 words, ending with a page id: `(AR p13)` or `(AR p13, p14)`. The page must be a business page.
2. Every number in a line is printed on a page that line cites. Copy a number exactly or leave it out. Do not round, convert or add up.
3. State only what the company is, makes, sells, to whom, and where. No future tense, no plans, no targets, no aims, no outlook, no guidance, no words such as will, expects, aims, plans to, targets.
4. No praise. Say what the company does, not how good it is (no leading, best, strong, robust, world-class).
5. Do not copy the report's sentences. Rewrite each in your own short plain words. Six words in a row must not match anything the company said on its calls or decks.
6. No management claim and no quote.
7. Chapter 2 says how the money comes in: which businesses, what each sells, who buys, and how big each is where a page prints it. It may name the three reported segments and what each does.
8. Chapter 7 lists only terms that belong to this company's own world and are not in the shared glossary (`references/glossary.md`), for example a product type or a business name. Each term gets one plain meaning and a page id. Do not repeat a shared term.
9. No em dashes. Plain words. Define a hard word the first time it appears, inside the same line.

**Length.** Chapter 1 about 8 to 12 lines. Chapter 2 about 10 to 16 lines. Chapter 7 about 6 to 12 terms.

**Then.** Run the checker, fix every FAIL, run it again. Then one clarity pass reads the chapters as a 15-year-old and sends anything unclear back for a plain-words rewrite.
