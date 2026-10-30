# Free-model build of the BIOCON seat, compared with the existing seat (2026-10-30)

Test only. The live seat (`.claude/skills/roast-room/brains/biocon-management/`, `.claude/agents/council-biocon.md`) was not changed; `git status` showed 0 changed files throughout.
Scripts: `scripts/free_seat_test/`. Raw sources and outputs stay in `build/biocon-free/` (gitignored).

## What was built
25 NSE sources (14 calls, 11 decks; the annual report S026 was not used). Code cut each call into speaker turns and kept management only (the call's own
participant block decides who is management). `nvidia/nemotron-3.5-lightning-30b-a3b` (thinking off) proposed quotes; code kept only quotes found verbatim in the
turn and took speaker, source and held date from the turn. Three full runs (3,000, 1,500 and 1,000-word batches): 498 extraction calls (106 + 166 + 226) plus a few topic-sorting calls, about 1.5M NVIDIA tokens, no Claude tokens.
The model's own proposals were verbatim 75 to 79% of the time; the rest were dropped by code.

## Coverage of the existing brain (456 of its 475 distinct quotes are findable in the freshly fetched sources)
| Run | same words as an existing quote | within about 300 characters of one |
|---|---|---|
| 3,000-word batches | 37% | 70% |
| 1,500-word batches | 41% | 79% |
| 1,000-word batches | 46% | 83% |
| union of the three | 66% (300/456) | 93% |

Scorecard statements (record.md, 36 findable): 24 exact, 36 nearby. Speaker agreement on matched quotes: 278 of 279.
Two-call side test on S008 and S009 (77 existing quotes): 1,500-word lightning 30; `nemotron-3-ultra-550b-a55b` 24, 99% of its proposals verbatim, about 3x slower.

## Quality limits of the free build
- Unranked: 2,733 distinct verified quotes against 475. A 30-item hand sample of free-only quotes: about 23 valid management statements, about 7 mislabeled or filler (a Safe Harbor line as "voice", past results as "commitment"). A rough sample, not a measured precision.
- No filed quarters, price, annual report, kept/missed scorecard or changes file. `_hot.md` is code-built (the 8 newest stated rules). Topic sorting leaves "Other" the largest bucket.

## Persona test (same agent file, two brains, Sonnet, three questions)
| Question | Existing seat | Free-model seat |
|---|---|---|
| Debt or new plant | Debt first. 6 cited quotes, plus filed S026 figures, the scorecard and a "what demand is unserved" question | Debt first. 8 cited quotes, 4 dated; says plainly that filed numbers and the scorecard are not in this build |
| Reliability of dated promises | Counts from the scorecard: 13 settled, 9 kept, 4 slipped, slips named with days late | Own count of 12 statements (3 kept, 5 slipped, 4 open), labelled "not a scored result"; says outcomes need filed facts |
| SaaS price rise (off topic) | Abstain, read only `_hot.md` | Abstain, read only `_hot.md` |

Quote check by script (verbatim in the fetched sources): existing 9 of 10 quotes cited to a source id are verbatim (the tenth is a short fragment paraphrased inside quotation marks "largely maintenance" for "mainly the maintenance capex"); free 18 of 19 verbatim (the other is a composed phrase, "advanced progress sometime next calendar year"). Checker false alarm: a 2-word quote is below its 3-word floor. Numbers and counts in the answers were not re-verified.
Cost note: each persona consult read about 230k to 290k subagent tokens either way, so the free brain is not cheaper to consult.

## Reading
The free build reproduces the "what was said, by whom, when" half well and keeps the persona's habits (first person, as-of line, abstain, what is unchecked).
It does not do the "what was filed and did it hold" half: scorecard outcomes, filed quarters and annual-report tables are missing, and nothing was tried to fill them.
Not yet tested: a Claude pass over the raw items to rank them and write `_hot.md` and the scorecard; a second company; a person seat.
