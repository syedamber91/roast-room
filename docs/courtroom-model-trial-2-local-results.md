# Trial 2 results: local (self-hosted) model for convict turns (2026-10-31)

**Result: FAIL at gate 2 (speed) for both models tried (`qwen3.5:9b` and `qwen3.5:4b`). Gate 1 (hardware) also failed. No convict turn was scored.**

Update 2026-10-31, after the owner asked to measure the speed anyway: `qwen3.5:9b` did not finish one real 55,000-token convict prompt within 330 seconds on the VPS. See "Measured: one real prompt" below. The first draft of this file (stop at gate 1, nothing run) is kept further down for the record.

Plan and gates: `docs/handoff-local-models-vps-test.md`. Hosted-model results for comparison: `docs/courtroom-model-trial-1-results.md`. The hosted bars were not changed. No new bars were registered, because the run stopped at the speed gate before any turn was scored. The 5-minute speed bar comes from the handoff plan, step 3.

## Measured: one real prompt (gate 2, step 3 of the plan)

Run by the soic-ladder job `local-model-timing` (PRs 1283 and 1285; report `docs/reports/local-model-timing/timing-2026-08-30.md`, measured 2026-10-31 19:15 to 19:22 UTC). Model `qwen3.5:9b` through Ollama (default tag; its quantization is not shown on the Ollama page). The prompt was issue I5, turn A1, built by `model_trial.build_prompt`: 227,531 bytes, about 55,000 tokens by my first estimate, later measured at about 70,000 (see the short-slice test).

| Item | Value |
|---|---|
| Download | 6,550,826,638 bytes in 94 seconds (files deleted after the run) |
| Settings | 65,536-token context, 3 threads of 4, nice 19, flash attention on, KV cache q8_0, 200 tokens requested |
| Time cap | 330 seconds (the 5-minute bar plus 30 seconds of slack) |
| Outcome | **Not finished within 330 seconds** (curl exit 28). Over the 5-minute bar. FAIL |
| Lowest free RAM during the request | 2,530 MB, from about 11 GB before |
| Steal before / after | 6 percent / 1 percent |

### Second model: `qwen3.5:4b` (same job, same prompt, same settings)

Soic-ladder PR 1286, measured 2026-10-31 20:27 to 20:34 UTC, dispatched by hand with the model name as the `companies` input.

| Item | `qwen3.5:9b` | `qwen3.5:4b` |
|---|---|---|
| Download | 6.55 GB, 94 s | 3.32 GB, 36 s |
| Outcome | Not finished in 330 s | **Not finished in 330 s** |
| Lowest free RAM during the request | 2,530 MB | 6,299 MB |
| Steal before / after | 6% / 1% | 0% / 1% |

The 4B model had plenty of memory left (6.3 GB free) and still did not finish, so on this box the limit is CPU speed, not memory. Halving the model did not bring one prompt under 5 minutes. Models smaller than 4B were not tried, and the hosted trial suggests they would score worse on substance.

What the 9B run does and does not show (the 4B run has the same limits: no progress output, load time inside the cap, quality not scored, licence not checked):
- It shows this model, on this CPU, does not return one convict prompt in 5 minutes, so the plan says stop.
- It does not show how long it would take. There was no progress output, so 6 minutes and 60 minutes look the same here. Model load time is not reported separately and is inside the 330 seconds.
- It does not test other models beyond the two above.
- The licence of `qwen3.5:9b` is not stated on the Ollama pages read and was not checked.
- Quality was not scored, because no answer came back.

### Short-slice speed test: `qwen3.5:4b` (soic-ladder PR 1287, measured 2026-10-31 21:31 to 21:41 UTC)

Four requests built from slices of the real prompt, 16,384-token context, 3 threads, 40 tokens written, 240 s limit each. Token counts are the server's own.

| Request | Tokens read | Reading speed | Writing speed | Wall time |
|---|---|---|---|---|
| 1 cold, about 2k tokens | 2,589 | 46.6 tokens/s | 12.3 tokens/s | 63 s |
| 2 same 2k start, new question | 2,587 | 103.5 tokens/s | 13.2 tokens/s | 28 s |
| 3 cold, about 6k tokens | 7,331 | 32.8 tokens/s | 7.7 tokens/s | 226 s |
| 4 cold, about 14k tokens | n/a | n/a | n/a | Timed out at 240 s |

Findings:
- **Reading the prompt is the cost, and it slows as the prompt grows** (104 tokens/s at 2.6k tokens, 33 at 7.3k, not finished at about 17k tokens by the same ratio). Writing speed is 8 to 13 tokens/s, so a 1,500-token answer would take about 2 to 3 minutes (my arithmetic, not measured).
- **The prompt is about 70,000 tokens, not 55,000.** 8,277 characters read as 2,589 tokens and 24,676 as 7,331 (3.2 to 3.4 characters per token), so 227,531 characters is about 67,000 to 71,000 tokens. Earlier text in this file saying "about 55,000 tokens" was an estimate and is too low. This also means the two full-prompt runs above, which used a 65,536-token context, may have had the prompt cut off. They were too slow either way, but they were not clean tests.
- **Best case for the full prompt is about 11 minutes** (70,000 tokens at the best speed seen, 104 tokens/s). At the 7k speed it is about 35 minutes. Both are far over the 5-minute bar.
- **The shared start was not reused.** Request 2 re-read 2,587 of 2,589 tokens. Cause unknown (model type, Ollama version or settings). So the 15 turns do not get cheaper from a shared start in this setup.
- **Run-to-run noise is large:** the same-sized start read at 47 and then 104 tokens/s. One run per setting is not a stable speed.
- **What would be needed:** a prompt about 10 times shorter (6 to 8k tokens, about 3 to 4 minutes of reading for the 4B model), which means sending only the files each turn needs. Whether answer quality survives that is untested. This is not a recommendation to proceed.

## Earlier draft: what was measured before the speed run

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
- This draft expected the speed bar to be missed; the speed run above confirmed it for `qwen3.5:9b`.
- The hosted trial already shows size matters. Lightning 30B with the retry loop escalated 10 of 15 turns and matched Sonnet's state on 2 of 15. A 7 to 14B model is very likely worse (the handoff's own expectation, not tested here).
- The best hosted run, Nemotron 3 Ultra 550B with the loop, still failed the bars: 1 invented quote (bar 0) and 9 of 15 states matching Sonnet (bar 12).
- The VPS was host-throttled to 20 percent CPU on 2026-09-26 after sustained heavy load, and the un-throttle works once per 7 days. A long CPU run risks that for a result that is unlikely to pass.

## Privacy note

This courtroom uses public filings only, so hosted models are acceptable here. A local model is only needed for private data. That need was not tested.

## What would change this

A VPS with a GPU or at least 32 GB of RAM. The owner first chose to stop, then asked for the timing run; it failed (above).

## Side findings

- The soic-run workflow's `actions/upload-artifact` step failed on every soic-run of this work (warm-up, hardware, timing). The jobs themselves succeeded. Cause not investigated.
- The warm-up `tests` run failed in its test step after about 19 minutes. Cause not investigated; it did not affect this result.

## Open owner questions (carried from the handoff, unanswered)

Target number of companies per month; the third company after PIIND; whether T1, T5, T6 and T7 proceed after this test.
