# Free-model build of the BIOCON seat, compared with the existing seat (2026-10-30, revised after review)

Test only. The live seat (`.claude/skills/roast-room/brains/biocon-management/`, `.claude/agents/council-biocon.md`) was not changed; `git status` showed no change there throughout.
Scripts and tests: `scripts/free_seat_test/`. Fetched sources and outputs stay in `build/biocon-free/` (gitignored).
An independent Fable-tier review found flaws in the first version of this report. This version fixes the ones that could be fixed and lists the rest.

## How the free build works
25 NSE sources (14 calls, 11 decks; the annual report S026 was not used). Code cuts each call into speaker turns and keeps management only (the call's participant block names management; before the Q&A starts, an unknown label such as "Europe:" is a scripted sub-heading, not a new speaker). A free NVIDIA model proposes quotes. Code keeps only quotes found word for word in the turn and takes speaker, source and held date from the turn.
Claude was not used for the reading. Claude was used for the design, the review, a 98-item blind labelling and the persona runs.

## Fixes made after the review (all checked by script)
- **Splitter bug.** Scripted sub-headings were read as new speakers and their text was dropped (the commitment-dense Chair remarks most of all). Fixed with 3 unit tests, one written red first. Findable existing quotes went from 456 to 469 of 475 (99%). Six remain unfindable (they cross turn boundaries).
- **Prompt leakage.** The extraction prompt held example phrases taken from the existing brain ("first claim is to reduce debt", "core EBITDA", "like-to-like", "line of sight", "transient"). Removed, and everything re-run.
- **Agent-file leakage.** The free agent file still carried existing-seat facts (39 scored statements, two quarters with no call text, price and announcement dates). Rewritten from the free build's own contents.
- **Metrics with no control.** "Within 300 characters" scored 90% for random text, so the earlier "93% nearby" figure meant nothing and is withdrawn. `compare.py` now prints full-match and half-match recall beside a random-window null and exits non-zero unless the half-match lift is at least 20 points.

## Coverage of the existing brain (469 findable quotes), clean reruns on the fixed corpus
| Run | full match | half match | random null | lift over null |
|---|---|---|---|---|
| `nemotron-3.5-lightning-30b-a3b`, 1,500-word batches | 32% | 47% | 17% | 30 points |
| `nemotron-3.5-super-vl-120b-a12b`, 1,500-word batches | 23% | 32% | 13% | 19 points (below the 20-point bar) |
| union of the two | 42% | 59% | 25% | 34 points |

- Scorecard statements (record.md, 36 findable): union covers 21 (lightning alone 14, super-vl alone 16).
- Super-vl: 86% of its proposals were verbatim (lightning 78%), but it returned fewer items, used about 50% more tokens (788k against 523k) and took twice as long (1,494 s against 752 s). On an early two-call test it looked better (48% against 39% on 77 quotes); that run still had the prompt leak and one run per cell, so it was not repeatable.
- The earlier three-run union with the leaky prompt scored 64% half-match on the same denominator; the clean two-run union scores 59%. The two are not the same runs, so the gap is not a measured leak effect.
- Speaker agreement (about 262 of 264) mostly checks the splitter, since both sides read the speaker from the transcript label.

## Precision, blind second reader (98 items, 14 per kind, kind hidden, one Sonnet labeller)
- Valid management statements: 86 of 98 (88%). Bar set in review: 90%. Just missed.
- The pipeline's own kind label agreed with the second reader 34 of 98 times (35%). Bar 80%. Failed.
  By kind (agree/14): commitment 11, figure 11, position 5, story 3, framework 2, rule 2, voice 0. Voice quotes were valid only 7 of 14.
- Reading: trust "commitment" and "figure" labels; do not trust "framework", "rule", "story" or "voice" from this model. One labeller is not ground truth.

## Persona test (done BEFORE the fixes above; not re-run)
Same agent file, two brains, Sonnet, one run per cell. Q1 debt versus a new plant: both lean to debt first; existing adds filed figures and the scorecard, free states it lacks them. Q3 off topic: both abstained.
Q2 promise reliability: the existing seat gave scorecard counts. The free seat's own count (3 kept, 5 slipped, 4 open) disagrees with the scorecard on aspart (free: slipped; record.md: Kept) and used call dates as approval dates (2025-08-08 is the call, the approval was 16 Jul 2025). It labelled its count "not a scored result". The two are not comparable.
Quote check by script: existing 9 of 10 verbatim, free 18 of 19. Numbers and counts in the answers were not re-verified. One run per cell, not blind.

## What this does and does not show
- The free model can read the calls and the code can make every kept quote exact. Roughly half of what the existing brain picked is also picked by one clean run, and about 6 in 10 by two runs.
- It does not show the free build can replace the existing seat. The kept-or-missed scorecard, filed numbers, ranking into the eight rules and `_hot.md` were not built by a free model. The one time the free seat tried to score outcomes (Q2) it got one wrong.
- Not done: a persona re-run on the cleaned build; a check of every number and verdict in the persona answers against `record.md`; a second company.
