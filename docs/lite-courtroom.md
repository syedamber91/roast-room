# Lite courtroom (PIIND), explained simply

**What it is.** A cheap version of the courtroom. The questions are fixed (the 50 data-point questions). The answers come from the VPS data-point run, where Nemotron read the documents and code checked each figure is on the cited page. Code decides answered or refused. Nemotron only writes short judge notes, and code checks each note's quote is really in the answers (rewritten once, then dropped). Code works out the ceilings, trust score and position (`court_rules.py`). The judge can only lower a score.

**It is NOT the BIOCON hearing.** Different evidence, no model-written lawyer, no gates checked. Do not compare the numbers. Question 49 (FIFA) is a control: it must stay refused, and the run stops if it is answered. "Answered" means a figure was found on a cited page. It does not mean good.

**Run it** (from the repo root):

```bash
python3 .claude/skills/courtroom/scripts/lite_court.py --answers path/to/t6-ask-2026-08-30.md --out sessions/piind-lite
```

- `NVIDIA_API_KEY` set (VPS only): Nemotron (`nvidia/nemotron-3-ultra-550b-a55b`) writes the judge notes. About 8 calls, one per issue with answers.
- No key: it runs offline with no judge notes and says so (`judge: none`). Force it with `--judge none`. Force Nemotron with `--judge nemotron`.

**Judge runs.** With a key, the judge runs 3 times per issue at once and the LOWEST score counts (`--judge-runs N` to change). One run was noisy: the same answers gave 2 to 12 of 21. Notes must also pass code checks: the quote is in the answers, every number is written in the answers, and no note may claim arithmetic (sum, total, doubled) or a size comparison.

**Open flags.** `references/lite-flags.json` lists answers that conflict with another reading of the same figure (borrowings, finance cost, ROCE, ROE vs Screener). They show beside the question on the Receipts page and in the report. They never change a score and are not resolved: only Nemotron may read the documents, so someone must re-ask them on the VPS.

**You get** in the `--out` folder: `lite-report.html` (SOIC-style report), `lite-receipts.html` (per issue: question, figure, source, page, code-check status), `lite-result.json`.

**Tests** (offline, fake judge): `cd .claude/skills/courtroom/scripts && python3 -m pytest test_lite_court.py`

**Files:** `scripts/lite_court.py`, `scripts/test_lite_court.py`, `references/lite-issues.json` (which question belongs to which issue, written by hand; I9 and I10 have none, so they read "no data").

**Real run needs.** The answers file lives in the soic-ladder repo. To run the judge on the VPS, someone must check out this branch there and run the command above with the key in the environment, or add a `soic-run` job that does so. Not written here.
