# Filings-reading coach: decision record

Dated history of what the owner decided, so a later session never has to guess.
The framework itself is `docs/filings-coach/framework.md` (not written yet at the time of the entries below).

## 2026-11-09: scope and sources

- The owner asked for a leveled framework (Level 1 to Level N, tasks and subtasks) for reading transcripts,
  annual reports and investor presentations to find signals, backed by statements from books and from the
  SOIC course, and then a new roast-room council seat built on it.
- Model routing set by the owner: cheap reading by Haiku or Sonnet; framework creation, framework generation
  and seat creation by Opus.
- Seat role chosen: **filings-reading coach**. It teaches and applies the leveled method and says what to
  check next. It gives no buy, sell or hold calls (the existing `council-analyst` seat already scores those).
- Books: the owner asked to download "everything possible". Only free and legal sources were downloaded
  (author or publisher sites, regulators, Project Gutenberg, archive.org public-domain items, US works
  published before 1931). Paid books from piracy mirrors were refused. Manifest with URL and legal basis for
  every document: `build/filings-coach/books/manifest.jsonl` (gitignored corpus; manifest to be committed).

## 2026-11-09: Round 1 (all recommendations accepted)

1. Audience: the ladder starts from zero and climbs to expert.
2. India-first: SOIC and Indian documents drive each step; US classics back or add.
3. Each subtask has: document and section, what to check, why, red flag, green flag, cited number (if any),
   citation, and a "done when" line. Each level ends with an exit test on a real filing.
4. Number of levels decided by the evidence, within 5 to 9.
5. Numbers only when a source states them, cited; worked-example numbers labelled as examples. Where
   `soic-ladder/rulebook/soic-ladder-rules-v1.yaml` states the same metric, the rulebook value wins.
6. Disagreeing sources are shown side by side, cited, with no verdict.
7. A book check whose short quote cannot be matched word for word against its page is dropped and logged.
8. One worked example company runs through every level, from the owner's Drive annual reports, built after
   the framework is approved.
9. Output: this folder (markdown, committed) plus a private page for reading.
10. Downloaded corpus stays local and re-runnable; only the manifest is committed.
11. Books: Sonnet reads the core set in full; Haiku reads the pre-1931 classics.
12. Local OCR (tesseract through `media_core.pdf_text`) recovers scanned documents.

## 2026-11-09: Round 2 (all recommendations accepted)

1. Levels are named by what the reader can do after them ("Level N: ...").
2. Levels climb by skill, not by document; each step names the document and section.
3. At most 6 tasks per level and 6 subtasks per task; overflow goes to a "Deeper checks" appendix, not deleted.
4. Sector-specific checks go to sector packs (one appendix per NSE sector), linked from the general step.
5. Banks, NBFCs and insurers get a marked "Lenders" subtask wherever the general step does not apply.
6. Citations are readable inline; internal ids live in an appendix lookup table.
7. Pre-1931 classics appear in a "Lessons from market history" box per level, never inside steps.
8. Exit tests are written generically now and made concrete with the worked example company later.
9. No time estimates per level (no source states one).
10. One-page checklist per level in an appendix.
11. Pipeline scripts are committed under `scripts/filings-coach/`; the corpus is not.

## 2026-11-09: standing requirement on growth

The owner: as more sources and content are added, the framework must evolve and update **incrementally**
from the new data, and this must be built into the current work, not added later. Consequences for the
build (see Round 3 for the open choices):
- every source and every extracted check carries a stable id and a content hash, so a re-run reads only
  what is new or changed;
- every framework step carries a stable id, and a mapping file records which checks support which step;
- adding a source produces a proposed change (new support for existing steps, new steps, new conflicts)
  instead of a full rebuild.

## 2026-11-10: Round 3, incremental growth (owner: "yes to all, go with your recommendations")

The questions were not shown to the owner before this answer; these are the recommendations the answer
accepted, stated back to the owner in the same reply:
1. A new source never edits the framework directly. It produces a **proposed change** (new support for
   existing steps, new steps, new conflicts, retired support), which the owner approves before it lands.
2. New sources go into one drop folder, `build/filings-coach/inbox/` (a matching Drive folder can be added later).
3. The framework carries a version number, and every accepted change adds a dated changelog entry.

## Counts at the time of these entries (2026-11-09)

- SOIC: 517 notes read, 3,023 checks extracted, 2,925 citations verified by timestamp, 1 dropped.
- Books: 140 readable documents (126 native text, 14 by local OCR, 1 of them force-OCR'd for a broken font),
  3,705 checks, all 3,705 quotes verified word for word against their pages.
- Partial reads, recorded as such: Clews (both halves), Lefevre/Crump/Duguid/Smith (C-7), Mackay second half,
  Bagehot, SEBI financial-education booklet, SEBI investor reading material.
