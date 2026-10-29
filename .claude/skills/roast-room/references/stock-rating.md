# Stock rating mode (council-owned trust table)

Used only when the decision is a rating call on one listed Indian stock: the options are A Buy (or add), B Wait, C Sell (or do not buy), and the India Market Analyst seat is at the table. The Chair turns it on in Step 2 and says so in `brief.md`. Any other decision runs the normal flow and ignores this file.

**The rule that matters:** the section numbers belong to the whole council, not to the Analyst. The Analyst proposes the first numbers and carries the questions. Every seat can agree, dispute or move a number, and the Chair publishes the council's final numbers. No seat's number is final by itself.

## What is rated: trust in management's word

The table rates how far management's word can be trusted. It does not rate price. Price is judged by the option scores, mainly by Buffett and SOIC when seated. The Analyst card states "valuation not scored here".

Seven sections, each scored 0 to 3. No weights.

| ID | Section (questions.md) | Lender set |
|---|---|---|
| S1 | Guidance versus delivery (section 1) | same |
| S2 | Earnings quality and accounting (section 2) | same |
| S3 | Cash, receivables, working capital (section 3) | replaced by lender asset quality (section 8) |
| S4 | Debt and funding (section 4) | read as funding: deposit quality and covenants only |
| S5 | Related parties and group companies (section 5) | same |
| S6 | Promoter: pledge, selling, succession (section 6) | same |
| S7 | Board, auditors, independent directors (section 10) | same |

Regulation (section 9) and capital allocation (section 7) are not scored. They only raise or clear a gate (below). Sections 11 and 12 of questions.md are not scored either.

**The 0 to 3 ladder (the same for every seat):**
- 3: every core question in the section is answered with a number and its date in the brief, and no red flag from checks.md fires.
- 2: answered with numbers, and one flag fires with a reason stated in the brief.
- 1: partial (words but no number), or a flag with no stated reason.
- 0: deflected, declined, or the brief has nothing.

Each number carries a state word: `answered`, `partial`, `deflected` or `no data`. A 0 for "no data" and a 0 for "declined on three calls" mean different things and both stay visible.

A company that states a no-guidance policy: S1 scores 2 if it gives another numeric anchor, 1 if it gives none (questions.md Q1.7).

**Evidence rule.** Company facts come only from the brief. A seat may score a section only from a line in the brief or a dated source in its own brain, and must name which. No seat may lift a number because its pillar likes the company.

## How the council sets the numbers

- **Round 1.** Every seat's card adds `SECTION SCORES: S1 n (state) · S2 n (state) ...`, and `-` for any section where it has no basis. The Analyst fills all seven and names the brief line or source behind each. It also adds `GATES RAISED:` (a gate letter, the document and its stage, or `none`).
- **Chair notes after Round 1.** The Chair builds the trust table: for each section, every seat's number, the median and the spread. Any section with spread 2 or more is a candidate crux. The Chair puts the widest ones (at most three in all, counting the ordinary cruxes) into the Round 2 prompt.
- **Round 2.** Each seat answers `SECTION DISPUTES:` for each disputed section: its number, the evidence (brief line or source id) and what would move it. A seat moves a number only for a better argument or a new fact, and says which. The Analyst also states which of its questions got answered.
- **Round 3.** `draft-resolution.md` carries the table as it stands. A seat may add `SECTION AMENDMENT: Sn x to y, one line` or dissent from a number. Dissent on a section is reported, not hidden.
- **Final number per section.** The median of the numbers seats gave in the last round that scored it (a `-` is ignored). With an even count, take the lower of the two middle numbers. If fewer than three seats scored a section, it is marked `thin`. If only the Analyst scored it, it is marked `analyst only`. The Chair computes and never invents a number.

Why the median: one enthusiastic or one hostile seat cannot move it alone. Why the lower middle: the cost of trusting too early is higher than the cost of waiting.

## Gates (they override the total)

Any seat can raise a gate in writing, with the document and its stage. A gate stands when the Analyst or at least two other seats confirm the stage from the brief. A gate that stands is applied after the table, whatever the total.

| Gate | Trigger | Effect |
|---|---|---|
| G-A | A regulator finding (final or confirmatory order) of diversion or misstatement | Sell leans 7 or more |
| G-B | Auditor resigned before term, reasons not read or citing non-cooperation | Sell leans 7 or more |
| G-C | Pledge invoked, or above the SEBI reason line with no stated reason | Sell leans 7 or more |
| G-D | Related-party flows well above the approved ceiling | Sell leans 7 or more |
| G-E | Interim order or show cause notice only, or a first loss estimate still unvalidated | Caps at Wait |

An interim order is an allegation, not a finding. Keep the two apart (frameworks.md section 3).

## Coverage and bands

- **Coverage** = sections with any data in the brief out of 7. Print it beside the rating, never inside it: `Trust 14/21, coverage 5/7, gates standing: none`.
- **Bands** (the seat's own, uncalibrated, not from any source): 18 to 21 answered and clean; 12 to 17 answered with open flags; 7 to 11 mostly partial; 0 to 6 unanswered or declined. A gate overrides the band.
- Every printed band carries the words: `seat's own bands, not from any source, uncalibrated`. This stays until the pre-registered check below has been run and passed.
- Most briefs will land in the low bands. The Analyst's own corpus shows only 60 of 269 analyst questions got a direct answer (questions.md section 13). That is the honest result. Do not tune the ladder to push scores up.

## How the rating feeds the Buy, Wait and Sell call

- The option scores come from the seat cards as usual (scoring.md). Trust is a separate number and is never an option score.
- **Trust cap (override, applied with the others in scoring.md).** The Chair may not recommend A Buy when a gate stands, when the trust rating is below the 18 to 21 band, or when the brief has no current price and latest results. The Chair then recommends B Wait and uses the WAIT label, naming the trigger that turns it into Buy and the date.
- **Wait list.** A stock with trust 12 or more, no gate standing, held at Wait only because price or results are missing, is printed as `Wait list: trust good, entry not yet`. This is a printed label, not a new number.
- The report prints the final table (template below) and says which sections moved in debate.

## Report block (goes in verdict.md after the Scorecard)

```markdown
## Trust table (council numbers)

| Section | Final | State | Seat numbers | Spread | Moved? |
|---|---|---|---|---|---|
| S1 Guidance | 2 | answered | Analyst 2, Buffett 2, SOIC 3, Bezos - | 1 | no |

Trust 14/21 · Coverage 5/7 · Gates standing: none · Seat's own bands, not from any source, uncalibrated
```

The room's JSON files have no field for this, so the table lives in `verdict.md` only. Put one line about any standing gate in `verdict.json` `override_note`.

## Pre-registered check (set before any real use; NOT YET RUN)

Take the 10 governance cases in `brains/india-market-analyst/stories.md` (A1 to A10). Score each on the 0 to 3 ladder from its "What was visible earlier" lines only, blind to the outcome paragraph, and write the predicted band down first. Pass bar: at least 7 of the 10 land at 11 or below, or hit a gate, on the earlier data. Fail means the bands are not usable and the card drops them.

Limits to state with the result: those cases were chosen because they went wrong, so a pass shows the rating notices trouble, not how often it raises a false alarm. A second check after three real councils: the Chair lists each seat's rating next to the verdict, and if the table and the Round 2 cruxes disagree on which section was the problem in two of three, the sections are mis-scoped.
