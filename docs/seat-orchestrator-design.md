# Seat orchestrator: Nemotron runs company-seat extraction end to end

Status: design opinion, 2026-11-09. No code. Written by the Opus advisor from the spec, the onboarding checklist,
`piind-seat-plan.md`, the PIIND blind check (soic-ladder-roster commit 4f2b7fa, `BLIND-CHECK-2026-11-08.md`),
headers of `datapack.json`, `nvidia_client.py`, `lite_court.py`, `soic_run.sh`, `soic-run.yml`, and the System One
playbook (iCloud vault `08-playbook/`). No PIIND document was read. Own synthesis is marked [inference].

## 0. The answer in one paragraph

Let Nemotron do the reading and the *choosing inside a menu*, never the *bookkeeping*. Code computes what is missing
(a diff of a fixed manifest against the folder and the ledger). Code owns the list of step types, the tier each
step may use, every bar, and the escalation path. Nemotron picks the order of the open steps, picks among the
tiers a step allows, proposes re-search targets for `not_stated` fields, and diagnoses a failed bar by choosing
causes from a fixed list. Claude models appear only as **labelled blind graders** whose output can lower a row's
status, never write a row, never plan, never pick a model. A failed bar triggers a fixed recovery recipe, at most two
cycles, then the field ships with its limit stated.

## 1. What Nemotron can decide, what stays in the manifest

| Decision | Owner | Why |
|---|---|---|
| Which fields/documents exist for a seat | code manifest (FIELDS.yaml + datapack.json lines + step registry), owner-approved | A list is not a judgement. An LLM asked "what is missing" invents gaps and drops real ones; a set difference cannot. |
| What is missing now | code: `manifest - (inventory ∩ ledger.done)` | Exact, repeatable, testable. |
| Order of open steps | Nemotron, from the code-made open list | Low-stakes; a bad order costs time, not truth. Code keeps a dependency check. |
| Tier for a step | Nemotron, only from the step's `allowed_tiers`; default when the reply is invalid | Keeps "Nemotron decides which tier" true while making a forbidden tier impossible. |
| Where to re-search a `not_stated` field | Nemotron proposes pages/sections; code runs the search and verifies | Same pattern as `lite_court.py`: model proposes, code verifies. |
| Why a bar failed | Nemotron picks from a fixed cause list; code computes the confusion table it reads | Free-text diagnosis drifts; a closed list is checkable. |
| Bars, prompts' fixed parts, label definitions, sample seeds | owner (pre-registered file, hashed into the ledger) | A planner that can touch its own bar will pass it. |
| Marking anything done | code verifier only | No model may close a step. |

How a free-roaming planner goes wrong, and the guard for each:

- **Hallucinated gaps** (invents "missing credit-rating rationale" or a FY that does not exist): gaps are computed, not
  asked. Nemotron may file an `advisory_gap` (new document type) that lands in the PR for the owner; it is never executed.
- **Silent skips**: every manifest field must end in one of `found | not_stated | not_applicable | unreadable | open`;
  the coverage report lists all of them every tick. A step the planner never picks stays `open` and visible.
- **Loops**: a step key that failed twice is frozen (`blocked`) and removed from the menu; a tick with zero new `done`
  keys ends the run as `stalled`. No self-dispatch.
- **Cost runaway**: per-tick caps on calls and tokens (section 5), read from API usage by code.
- **Grading its own homework**: a second Nemotron pass measures repeatability, not accuracy ("repeatability read as
  accuracy", vault `anti-patterns.md`). The grader is always a different model family.
- **Agents writing their own questions**: the vault records "agents aren't great at writing questions"
  (`anti-patterns.md`, from `typesafe-agent-skill`); so Nemotron never writes the bar's questions or definitions,
  only proposes revisions for the owner.

Autonomy recommendation: **level 2 of 4** [inference] — (1) fixed script, **(2) model chooses within a code menu,
code verifies, owner approves spec changes**, (3) model may add steps, (4) model sets bars. Level 2 is honest to
the owner's rule (no Claude decision anywhere in the loop) and still checkable. Be candid with the owner: for most
of a seat the plan is a dependency sort, and a deterministic default plan will be nearly as good. Log Nemotron's
plan beside the default and measure whether it ever helps (section 6).

## 2. Architecture

```
inputs (manifest, datapack.json, folder inventory, ledger)
   -> GAPS (code diff)
   -> PLAN (Nemotron chooses from menu; schema + allowlist check; fallback = default plan)
   -> EXECUTE (one step = many units; each unit idempotent)
   -> VERIFY (code bars: verbatim, sums, planted-wrong, enum, coverage)
   -> LEDGER (append-only JSONL) -> PR (never merged by the job)
   -> [optional] GRADER PACKET for a blind grader outside the VPS; its result file is read next tick
```

Step registry entry (owner-approved, in the repo, hashed):

```json
{"step_type": "qa_states", "doc_class": "CALL", "fills": ["T16"], "datapack": ["D11"],
 "needs": ["calls_mgmt_turns", "qa_pairs"], "allowed_tiers": ["nemotron"], "default_tier": "nemotron",
 "unit": "one call", "verifier": "qa_states_check", "bar_id": "BAR-QA-01",
 "grader": {"tier": "sonnet-blind", "sample": 40, "seed_from": "bar"}, "escalation": "RECIPE-LABELS",
 "max_attempts": 2, "cpu_heavy": false}
```

Inventory (code, from the folder; sha256 pins the input):

```json
{"company": "PIIND", "as_of": "2026-11-09",
 "docs": [{"class": "CALL", "id": "CALL-2026-08", "path": "data/calls/....txt", "sha256": "…", "mgmt_turns": 52}]}
```

Gap (code):

```json
{"step_type": "qa_states", "unit": "CALL-2026-08", "reason": "no ledger done key for inputs sha …",
 "blocked_by": [], "fields": ["T16"]}
```

Plan (Nemotron reply; code rejects anything not matching the schema or the allowlist):

```json
{"plan_version": 1, "steps": [
  {"step_type": "qa_states", "unit": "CALL-2026-08", "tier": "nemotron", "why_code": "UNBLOCKS_DATAPACK"},
  {"step_type": "segments_pdf", "unit": "RES-2025-09", "tier": "code", "why_code": "CHEAP_FIRST"}]}
```

`why_code` is a closed enum (`UNBLOCKS_DATAPACK | CHEAP_FIRST | REQUIRED_FIELD | RETRY_AFTER_FIX`), not prose.

Ledger line (one per unit attempt):

```json
{"key": "sha256(step_type|unit|inputs_sha|config_sha|model_id)", "step_type": "qa_states", "unit": "CALL-2026-08",
 "tier": "nemotron", "model": "nvidia/nemotron-3-ultra-550b-a55b", "config_sha": "…", "status": "done|failed|unreadable|blocked",
 "verifier": {"quotes_verbatim": "88/88", "enum_ok": true, "planted_caught": "6/6"}, "out": "record/qa-states-CALL-2026-08.csv",
 "calls": 14, "tokens_in": 0, "tokens_out": 0, "seconds": 0, "ts": "…"}
```

How a step names its tier: the plan names it, the registry bounds it, the ledger records the model id that actually
answered (log `response.model`, per the System One rule on pinning versions). A step with `allowed_tiers: ["code"]`
can never reach a model.

## 3. Tier routing (onboarding checklist items)

Rule of the table: **extractor** writes rows; **checker** can only lower a row (to `unverified` / `contested`) or
fail a bar. Claude tiers are checkers only, always labelled `grader:sonnet` / `grader:opus` in the file.

| Work | Runs it | Checks it | On a failed bar |
|---|---|---|---|
| Fetch (NSE API, archives) | code | code: sha256, size, page count, label count in window (checklist trap "label trap") | retry policy in code; else `unreadable` with reason |
| XBRL parse (results, shareholding, segments) | code | code: sums tie, YTD-context check, schema normalise (checklist traps) | mark row failed, never repair |
| PDF table parse | code (`pdftotext -layout`, `pymupdf4llm`) | code: sums, cell count per line | `unreadable`; use another filing's comparative column |
| Scan reading (promoter letters, scanned results) | **open question**: code OCR then Nemotron reads OCR text, tier `ocr-unverified` | code sum check on any number; blind grader on a sample of letters | stays unread and listed. Whether Nemotron Ultra takes images was NOT checked |
| Speaker split / management turns | code (`case_study_management_text.py`) | code: turn counts vs header roster; planted mislabeled turn | reader fix (test first), never model |
| Candidate sentence selection | code regex + optional Laya (local) or Jev filter | recall check on a labelled sample | widen to all sentences; do NOT put an embedding page-finder in front of long PDFs (vault `anti-patterns.md` G: it lowered accuracy, owner-measured) |
| Claim / statement extraction (calls, decks, AR prose) | Nemotron | code: verbatim in a management turn or page (2 readers = High), planted-wrong all rejected, foreign-company sentences all fail; then blind grader | RECIPE-QUOTES |
| Labels on extracted rows (driver, direction, Q&A state) | Nemotron | blind grader of another family (Sonnet), Opus adjudicates disputes as grader | RECIPE-LABELS (section 4) |
| Curated frameworks / stories / principles / voice | Nemotron drafts, each sentence tied to row ids | code: every quote verbatim, every paragraph cites ≥1 row; grader: "supported by cited rows?" Score | owner reads; no code can certify "fair summary". Defer |
| Review: re-search `not_stated`, audit unvisited sections | Nemotron proposes where, code searches page files (grep), Nemotron re-reads hits | code verifier | stays `not_stated` with the searched list |
| Final blind check | Sonnet blind grader, Opus adjudicator for disputes | the bar file, by code | report FAIL, ship with limit |

Jev vs Laya: PIIND filings are public, so the hosted privacy gate does not block Jev; Laya runs locally on the VPS
(laya jobs exist in `soic_run.sh`). Either is only a cheap filter or a typed second opinion, never the gate
(System One hard rule: advisory only). No System One tier for numbers, sums or dates (code). Laya degrades past
~20 options (vault `when-to-use-which-model.md`).

**Escalation and the owner's rule.** When Nemotron fails a bar, do NOT escalate extraction to Sonnet or Opus: that
is exactly the rule break. Escalation goes *sideways*, inside Nemotron (better context, narrower question, a `none`
option, smaller units), then *up to the owner*. Opus enters only as an adjudicating grader on disputed rows, and its
ruling may set a row to `checked` or `contested`; it never rewrites the label. To keep this honest:
(a) grader packets are built by code (seeded sample, definitions, same context window as the extractor), so the
Claude session cannot choose what to look at; (b) grader output goes to `checks/`, never to `record/`; (c) the
owner signs one line in the spec: "Claude may grade; never extract, plan, choose a model or write a record row."
Note this is a change: the owner's rule says *all reading* is Nemotron's; a blind grader reads 40 quotes. The PIIND
check already did this with Sonnet, so ask the owner to ratify it rather than assume it.

## 4. Worked failure: the 21 of 40 blind check

Facts (BLIND-CHECK-2026-11-08): bar 36/40 on driver AND direction; got driver 29, direction 30, both 21. All 11
driver disagreements are machine `demand` rows (7 of them reader `none`); `demand` is 177 of 291 rows. The grader
saw the quote alone; the machine saw two sentences each side. No adjudication. One sample, one grader, one run.
At n=40 the observed 52.5% has a 95% interval of roughly 37% to 67% [inference, Wilson interval computed by hand;
recompute in code] — far below 90% whatever the grader noise.

What the orchestrator does next, automatically (RECIPE-LABELS):

1. **Code diagnosis, no model.** Write the confusion table by label (done in the note by hand; make it code).
   Classify by fixed cause list: `context_mismatch` (grader saw less), `definition_overlap` (one label absorbs
   others: `demand` here), `missing_null_option` (reader `none` dominant: 7 + 5 cases), `grader_noise`.
2. **Fix the check before the extractor.** Re-run the grader on a *fresh* seeded 40 (never the same 40: re-testing
   on the failed sample tunes to it) with the same context window the extractor had. Same bar. Add an Opus
   adjudicator on the disputes (BIOCON's check did this). Both pre-registered before the run.
3. **If it still fails**, the cause is the label set. Nemotron proposes a revised definition set (e.g. explicit
   `none`, a narrower `demand`) as a file in the PR. **Owner approves** (spec change; not automatic). Then Nemotron
   re-labels all 291, a planted set (rows with a known label) must be caught, and a third fresh 40 is graded.
4. **Two cycles max.** Then stop: the table ships with "quotes verified, labels below bar (x of 40)" in the data
   pack `partial` note, exactly as BIOCON FY26 prose was accepted with its limit. The 291 quotes stand regardless.
5. Never: lower the bar, drop hard rows from the sample, let the grader's label replace Nemotron's, or call Sonnet
   to extract.

Steps 1 and 2 need no owner input and run in the next tick; step 3 waits on a PR approval (`waiting_owner`).

## 5. Guards

- **Time.** The VPS job limit is per job in `soic_run.sh` (`t6-lite-court` is 15 min; the caller reports a lite-court
  run took 27 min). Give the orchestrator its own entry (e.g. 45 min, illustrative) and a self-stop at job limit
  minus a margin. Work is in units; after each unit the ledger is flushed, so a timeout loses at most one unit.
  `nvidia_client.chat` already uses a 300 s timeout and 3 tries on 429/5xx; history: 29 of 132 Ultra calls died on an
  earlier 120 s limit (soic-ladder commit 000d37d).
- **Step budget per tick** (illustrative, tune after the first runs): ≤ 8 steps, ≤ 200 Nemotron calls, a token cap;
  stop and report when hit. One planner call per tick; an invalid plan is not retried, the default plan runs.
- **Idempotent resume.** Ledger key = hash of step type, unit, input sha256, config sha (prompt, definitions, bar),
  model id. A key already `done` is skipped; changing the prompt changes the key (so a re-run is explicit). Outputs
  written to temp then renamed. Files present without a ledger line are not trusted and are re-verified.
- **Host lock.** Nemotron calls are network-bound; don't put the whole orchestrator under the heavy-job `flock`
  (it would queue behind long jobs; `judge` alone is 4320 min). Steps marked `cpu_heavy` try `flock -n`; if busy,
  the step is deferred, ledgered as `deferred:host_busy`, not failed.
- **No merges, no self-dispatch.** Output returns as a PR (the workflow already does this, and refuses changes
  outside `--paths`). The job never merges, never dispatches itself; a cron, if added later, has a max-ticks count.
- **Secrets.** Planner and grader packets carry paths and excerpts only, never `.env` or keys; Claude graders get
  packets via the PR, not VPS access.
- **Reporting.** Each tick writes `orchestrator-tick-<n>.md`: gaps before/after, plan vs default plan, steps run,
  bars passed/failed with numbers, blocked keys, cost, what was not read.

## 6. Smallest first build: one VPS job, PIIND only

Job `seat-orchestrator --company PIIND --ticks 1`, paths limited to `docs/idea/case-study/PIIND/`.

Scope: manifest with ~6 step types already working for PIIND (shareholding, segments XBRL, segments PDF, results
XBRL/PDF as code steps; `qa_pairs` code; `qa_states` Nemotron on ONE call). Gap diff, one Nemotron plan, execute,
verify, ledger, PR.

Pre-registered success bar (all must hold; write it to the bar file before the run):

1. Code gap list for PIIND equals the hand gap list in `piind-seat-plan.md` sections 3 and 6 on every row both can
   express (owner reviews the mapping once, before the run). A mismatch is a finding, not a fail to explain away.
2. Planner: reply passes schema and allowlist, or the fallback runs and is logged; zero steps outside the menu run.
3. Planted tests, all caught: a planner reply naming `opus` as extractor is rejected; a planted output file with
   no ledger line is re-verified, not trusted; a planted unreadable PDF ends `unreadable` and listed; a planted
   wrong quote in the `qa_states` output is rejected by the verbatim check.
4. Kill-and-resume: the job is killed mid-step, re-run: no unit done twice, no unit lost, ledger consistent.
5. The tick ends inside its own time limit and under its call cap, with a tick report.

Not a success criterion in build 1: label quality of `qa_states` (that needs its own blind-check bar), nor whether
Nemotron's plan beats the default plan (log both; judge after ~10 ticks).

Defer: the RECIPE-LABELS automation (do step 1 and 2 by hand-run job first), AR prose FY22 to FY24 fetch, scans/OCR,
curated files, Opus adjudication packets, other companies, cron.

## 7. What I could not check

- FIELDS.yaml contents (soic-ladder branch `claude/company-record`; not opened), so the manifest shape is a proposal.
- Whether Nemotron Ultra accepts images (matters for scans); its per-call latency for a planning prompt; NVIDIA API
  pricing. No numbers for these are given here on purpose.
- Why the lite-court run took 27 min (likely judge runs × 3, not checked) and whether that pattern carries over.
- Whether Jev (TYPESAFE key) is available to the VPS orchestrator job; no `mcp__jev__*` call was made for this doc.
- Whether the blind grader or the machine is right on the 21/40 rows: no adjudication exists yet.
- The deeper premise: whether a Nemotron planner adds value over a dependency sort. The design makes that measurable
  rather than assumed.

Sources: `docs/company-seat-spec.md`, `docs/company-seat-onboarding-checklist.md`, `docs/piind-seat-plan.md`,
soic-ladder-roster 4f2b7fa `BLIND-CHECK-2026-11-08.md`, `.claude/skills/courtroom/scripts/lite_court.py` and
`nvidia_client.py` (headers), soic-ladder `scripts/soic_run.sh` (timeouts, flock), `.github/workflows/soic-run.yml`
(header), System One vault `08-playbook/anti-patterns.md`, `when-to-use-which-model.md`, `agent-operating-protocol.md`.
