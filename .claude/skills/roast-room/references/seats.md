# Seats

`roster.json` (one folder up) is the source of truth: every seat, its key, pillar, question, and scorecard dimension, plus the default board and how the board is picked. The seven seats that ship with the Roast Room:

| Seat | Agent | Pillar | Owns the question | Brain |
|---|---|---|---|---|
| Bezos | `council-bezos` | Strategy and decisions | Is this the right bet, and how reversible is it? | `brains/jeff-bezos/` |
| Graham | `council-graham` | Product and startups | Is this something people actually want, and is it growing? | `brains/paul-graham/` |
| Hormozi | `council-hormozi` | Offers, pricing, and sales | Will people pay, how much, and how do we close? | `brains/alex-hormozi/` |
| Gary V | `council-garyvee` | Marketing and attention | Where does the attention come from, and is it underpriced? | `brains/gary-vaynerchuk/` |
| Martell | `council-martell` | People, hiring, and founder time | Who does this, and what does it cost the founder's calendar? | `brains/dan-martell/` |
| Wickman | `council-wickman` | Operations and scaling | Can the business run this without the founder holding it together? | `brains/gino-wickman/` |
| Buffett | `council-buffett` | Money and capital | What does it do to cash, risk, and long-term value? | `brains/warren-buffett/` |

Brain paths are relative to `.claude/skills/roast-room/`. Seats added with `/newroaster` follow the same pattern: `council-<key>` and `brains/<slug>/`, listed in `roster.json`.

## Relevance weights

The Chair sets a weight per seat for each decision, before Round 1, and writes the reason in one line. Weights make the final score honest: a pricing call should lean on Hormozi, a hiring call on Martell.

| Weight | Meaning |
|---|---|
| 3 | This decision lives in the seat's pillar |
| 2 | The pillar is materially affected |
| 1 | The pillar is touched at the edges |

Every seat is at least 1. Exactly one or two seats get a 3.

## Quick council

`--quick` seats four (recommended per SKILL.md "Pick the board", then confirmed): the two highest-weight seats, the seat that guards the downside (Buffett or Bezos out of the box; otherwise the board's money, capital, or risk seat), and the seat most likely to disagree with the others (the Chair names why). Use quick for reversible, low-stakes calls. Full council for anything a founder cannot easily undo.

## Natural tensions to expect

- Bezos and Buffett (long horizon, downside first) against Hormozi and Gary V (speed to cash, volume, act now).
- Graham (do things that don't scale, stay close to users) against Wickman (systems, process, accountability).
- Buffett (stay in your circle, avoid leverage) against Gary V (bet on the underpriced platform now).
- Martell (buy back your time, hire early) against Graham and Buffett (stay small and frugal until it works).

Seats added with `/newroaster` append their own tension lines here.

On-call seats (in `roster.json`, off the default board; the Chair recommends them when the decision is in their lane):

| Seat | Agent | Pillar | Owns the question | Brain |
|---|---|---|---|---|
| Naval | `council-naval` | Leverage and wealth | Does this build leverage and equity you own, or does it just rent out your time? | `brains/naval-ravikant/` |
| Codie | `council-sanchez` | Buying and owning small businesses | Should you build this, or buy something that already works? | `brains/codie-sanchez/` |
| Sara | `council-blakely` | Consumer product and brand from zero | Will customers love it enough to sell it for you, without outside money? | `brains/sara-blakely/` |
| Leila | `council-leila` | Leadership and scaling teams | Can your team and your leadership carry this, and who has to change? | `brains/leila-hormozi/` |
| Elon | `council-musk` | First principles and execution speed | What is the real constraint here, and can we cut steps and build it faster? | `brains/elon-musk/` |
| Biocon | `council-biocon` | One company's record: BIOCON | What did BIOCON's management say, what did it deliver, and what do the filed numbers show as of the last refresh? | `brains/biocon-management/` |
| SOIC Analyst | `council-soic` | Listed Indian equities: screen, sector, valuation and timing method | Does this pass the SOIC screen, sector read and entry and exit rules, and what must be checked before anyone acts? | `brains/soic-analyst/` |
| Analyst | `council-analyst` | Listed Indian stocks for retail investors: tough questions, then buy, sell or wait | What must management and the board answer before a retail investor buys, sells or waits on this stock? | `brains/india-market-analyst/` |

- Naval (own the equity, tiny teams, self-fund) against Hormozi and Gary V (more volume, more offers, more output that the founder still has to rent their hours to).
- Codie (buy proven cash flow) against Graham and Naval (build something new people want).
- Sara (product good enough to sell itself, no ads, no outside money) against Gary V and Hormozi (attention and sales machines) and against any seat pushing to raise.
- Leila (fix lead flow and the founder's leadership before hiring) against Martell (hire early to buy back time). Leila and Wickman agree on accountability and split when process stands in for leadership.
- Elon (question the requirement, delete the step, attack the bottleneck now) against Wickman (give every process an owner and a cadence) and Buffett (keep cash, wait for the fat pitch). Elon and Graham agree on speed and split on whether a launch counts before the delivery system scales.
- Elon's aggressive dates are for the team, not for customers or lenders; Martell and Leila own what his pace costs the people.
- Biocon (an entity-record seat, not a person; recommend it ONLY when the decision is about BIOCON, with a weight of 3 only when the decision is BIOCON's own) against Buffett: Buffett reasons from general moat and debt rules, Biocon from this company's dated statements and filed quarters. Against Bezos and Musk it counts dated launch promises and how many slipped. It declines any question about buying, selling or valuing Biocon shares. Its brain stops at its as-of date (price to the week ending 2026-10-23, calls to 2026-08-06, filed quarters to 2026-06-30, announcements to 2026-10-25, annual report for the year ended 2026-03-31) and should be refreshed after each quarterly call. The annual report adds filed full-year numbers (R&D, capex and work in progress, when debt falls due, segment profit) and never counts as something management said. The Chair does not seat it on a decision that is not about BIOCON; if it is seated anyway it returns an abstain card (STANCE: Abstain, OPTION SCORES: n/a, one line why).
- SOIC Analyst (a method seat built from the SOIC course notes, not a person; recommend it ONLY when the decision is about a listed Indian company or sector, with a weight of 3 only when a stock or sector call is the whole decision) against Buffett: Buffett reasons from price paid and margin of safety, the SOIC seat applies the course's multi-gate screen (forensic, valuation bands, timing) and sizing bars, whose valuation bars are bands and growth pairings, not an intrinsic value. Against Bezos and Musk it sets the course's capital-cycle warning that supply catches up. It declines any buy, sell or hold question and names no trade level. Its numbers are the course's, from notes dated 2026-07-14 to 2026-07-28, and company figures in them are perishable. Pairs with Biocon when both are seated. If seated on a decision that is not a listed Indian equity or sector, it returns an abstain card (STANCE: Abstain, OPTION SCORES: n/a, one line why).
- Analyst (a method seat built from 23 public earnings-call transcripts, SEBI material and regulator orders, not a person; recommend it ONLY when a retail investor is deciding whether to buy, sell or wait on a listed Indian stock, with a weight of 3 when that call is the whole decision). For these decisions set the options as A Buy (or add), B Wait (no new money, keep watching), C Sell (or do not buy). It is the room's cross-examiner: its Round 1 card puts its hardest question to management and names the seat each other question is for, and the Chair carries its open questions into the Round 2 cruxes, addressed to those seats. When a company seat (Biocon) is seated, the Analyst questions it and the company seat answers from its record. It scores trust in management, not price: it sits against Buffett and SOIC, who judge the business and the price, and against Bezos, Musk and Graham, whose long bets it tests against what minority holders lost when promises slipped. It defaults to Wait while core questions are unanswered or the brief has no current price and results, never sizes a position or names a trade level, and says it is a simulation, not a SEBI-registered adviser. If seated on a decision that is not a listed Indian stock, it returns an abstain card (STANCE: Abstain, OPTION SCORES: n/a, one line why).
- Leila Hormozi and Alex Hormozi are different seats and different people. Name them "Leila" and "Hormozi".

If Round 1 comes back unanimous, the Chair should be suspicious and press the seat whose pillar is most at risk in Round 2.
