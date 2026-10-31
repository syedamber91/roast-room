# Trial 2 results: local (self-hosted) model for convict turns (2026-10-31)

**Result: stopped at gate 1 (hardware). No model was loaded and no convict turn was run.**

Plan and gates: `docs/handoff-local-models-vps-test.md`. Hosted-model results for comparison: `docs/courtroom-model-trial-1-results.md`. The hosted bars were not changed and no new bars were registered, because the run never started.

## What was measured

The VPS hardware, read by a new read-only soic-ladder job (`vps-hardware-check`, soic-ladder PR #1280). The runner's report is soic-ladder PR #1282, file `docs/reports/vps-hardware/hardware-2026-08-30.md`. The file name carries the snapshot date; the measurement time inside it is 2026-10-31 18:20 UTC.

| Item | Value |
|---|---|
| GPU | None. `lspci` lists none; `nvidia-smi` not installed |
| RAM | 15 GB total (`free -g` rounds down), 11 GB available, no swap |
| CPU | 4 cores, AMD EPYC 9355P, no GPU offload |
| Steal (`vmstat`, `st` column) | 1 to 2 percent during the 5-second sample |
| Disk | 30 GB free of 193 GB (85 percent used) |
| OS | Ubuntu 24.04.4 LTS |
| Tools present | python3, git, tmux, gcc, make, ollama (`/usr/local/bin/ollama`). Not found: llama-cli, llama-server, cmake |

## Gate 1

Rule from the handoff: no GPU and under 16 GB RAM means stop and report. The VPS has no GPU and 15 GB of RAM, so **gate 1 FAILED**.

## Why stopping is the right call, and what is not measured

- A 7 to 14B model at 4-bit would run on CPU only, on a shared 4-core box. The task is 15 prompts of about 55,000 tokens, with up to 2 retries per turn.
- **Not measured:** the time for one 55,000-token prompt. The expectation that it would miss the 5-minute bar is an estimate, not a result.
- The hosted trial already shows size matters. Lightning 30B with the retry loop escalated 10 of 15 turns and matched Sonnet's state on 2 of 15. A 7 to 14B model is very likely worse (the handoff's own expectation, not tested here).
- The best hosted run, Nemotron 3 Ultra 550B with the loop, still failed the bars: 1 invented quote (bar 0) and 9 of 15 states matching Sonnet (bar 12).
- The VPS was host-throttled to 20 percent CPU on 2026-09-26 after sustained heavy load, and the un-throttle works once per 7 days. A long CPU run risks that for a result that is unlikely to pass.

## Privacy note

This courtroom uses public filings only, so hosted models are acceptable here. A local model is only needed for private data. That need was not tested.

## What would change this

A VPS with a GPU or at least 32 GB of RAM, or a decision to run one timing test anyway (one prompt, capped with `systemd-run --scope -p CPUQuota=200%`, in tmux, not beside a soic-ladder heavy job). The owner chose to stop instead (2026-10-31).

## Side findings

- The soic-run workflow's `actions/upload-artifact` step failed on both runs of this work (the warm-up `tests` run and the hardware run). The jobs themselves succeeded. Cause not investigated.
- The warm-up `tests` run failed in its test step after about 19 minutes. Cause not investigated; it did not affect this result.

## Open owner questions (carried from the handoff, unanswered)

Target number of companies per month; the third company after PIIND; whether T1, T5, T6 and T7 proceed after this test.
