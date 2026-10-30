# Free-model seat build: test harness

Reference copy of the scripts used on 2026-10-30. They run from `build/biocon-free/pipeline/` (gitignored, holds the fetched
NSE sources). `urls.tsv` there comes from the live `sources.md`. Nothing here writes to `.claude/skills/roast-room/brains/`.

Order: fetch PDFs, `pdftotext -layout`, `split_turns.py`, `extract.py <model> <out.jsonl> [--max-words N]`, `merge.py`, `baseline.py`, `compare.py <out.jsonl>`.
`council-biocon-free.agent.md` is the live agent file with its brain root pointed at the test brain. Needs `NVIDIA_API_KEY`.
