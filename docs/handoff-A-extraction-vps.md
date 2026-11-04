# Handoff A: cheaper extraction on the VPS (read handoff-2026-11-04-master.md first)

Goal: do the extraction and lookup work that this chat did on Claude Code cloud on the VPS instead, with far fewer Claude tokens, using libraries, skills, GitHub repos and free models. RAG and the Obsidian knowledge are in scope.

## Where tokens went (measured only where stated)
- Courtroom hearing: ~397 KB hearing.md, ~20 agents killed mid-run by a usage limit and re-dispatched; Opus/Sonnet agents re-reading turn files; closings and judge notes rewritten. Not counted in tokens: unchecked.
- web-fetch subagents summarising pages (BIOCON Screener, Notion, peers); each ~35k subagent tokens.
- Re-reading annual report page files and grepping by hand.
- Model-free already: pdftotext/pypdf text, regex, python arithmetic, check_hearing.py guards, page builders.

## Existing assets to reuse
- soic-ladder VPS runner: scripts/soic_run.sh jobs (case-study modes fetch-results, fetch-calls, fetch-decks, fetch-annual-reports, annual-report-pages, qa-pairs, announcements, excerpts; deck-probe / transcript-check). Trigger: git push origin HEAD:run/<job>/<name>. A NEW job name must be on main first and one other run must finish before it resolves (docs/CLOUD-WORKFLOW.md). VPS CPU safety: flock + steal/load refusal; heavy jobs only via cpu_heavy_job().
- provenance repo = the RAG: PDF parse (rebuilt rows or find_tables per page), chunker (page-bounded), Ollama nomic-embed-text, SQLite FTS5 + vectors, RRF hybrid search, generate via OpenRouter, verify.py mechanical number check (+ null test). Never weaken verify.py; run null_test_verifier.py before/after any change.
- knowledge-toolkit: media_core.pdf_text is the ONE PDF reader (pypdf, then LiteParse OCR only for empty pages); tests/test_pdf_ingest_guard.py enforces it. soic-ladder pilot has an approved exception for PyMuPDF readers.
- Obsidian: learning-vault-invest (SOIC persona wiki, cited-quote gated), knowledge-toolkit vaults and graphify graph (graphify-out/GRAPH_REPORT.md), claude-memory MEMORY.md.
- Free models: NVIDIA NIM (Nemotron etc., key from $SOIC_ROOT/.env, never printed), results in docs/courtroom-model-trial-1-results.md; local models on the VPS: docs/handoff-local-models-vps-test.md (Qwen test plan; GPU not required for small models, unverified speed).

## Tasks
1. Map every step of the BIOCON refresh (fetch, extract, case book, hearing, report) as: model-free / free-model / Claude. Measure tokens per step on one real refresh; keep a cost log.
2. Move fetch + extract + case-book build to VPS jobs (no Claude); output committed small text/CSV so a cloud session can read it.
3. Search GitHub and existing skills for equivalents of what was done by hand (PDF-to-structured tables, filing/announcement fetchers for NSE/BSE, concall Q&A splitters, hybrid retrieval, claim-vs-source checkers). List candidates with licence, last commit, fit; test 2 to 3 on a fixed sample; do not adopt on a README alone.
4. Add retrieval over the BIOCON corpus (calls, decks, report pages, announcements) via the provenance pattern, plus Obsidian/graph routing; answer from top-k, verify numbers mechanically.
5. Replace web-fetch subagent summaries with raw-fetch + regex/table parse where a page is structured (Screener tables, NSE JSON).
6. Pick free models per step (extraction, classify, draft) with a golden set (the ten BIOCON issues and the 13 corrections found after the hearing); a model passes only if it matches or beats the current output on that set.

## Success measures
Tokens per refresh down by a stated factor; same answers on the golden set; every number still traceable to a page and date; no step silently falling back to memory.

## Pitfalls already paid for
Label traps (count in-universe and in-window); a page-doubling parse diluted retrieval; one run per cell is noise (use several reps, report range); tested verifier first, generator second; a read tool that fails silently (empty OCR page, 200 with a shell page); units (Rs million vs crore); correct year of report.
