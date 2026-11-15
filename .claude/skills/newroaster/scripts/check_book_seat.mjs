#!/usr/bin/env node
// Check a book seat's brain against its private store (owner decisions Q11/Q15, 2026-11-14).
// Every "quote" (ID) must be a word-for-word piece (under 45 words) of an item quote from that section, and every
// [full: ID] must name a real item. The store holds the book quotes, so this runs only where the private repo is cloned.
//   node .claude/skills/newroaster/scripts/check_book_seat.mjs <brain-dir> <items_final.jsonl>
import { readFileSync, readdirSync, existsSync } from "node:fs";
import { join } from "node:path";

const [brain, store] = process.argv.slice(2);
if (!brain || !store) { console.error("usage: check_book_seat.mjs <brain-dir> <items_final.jsonl>"); process.exit(2); }
if (!existsSync(store)) { console.error(`no private store at ${store}: clone roast-room-private to check quotes`); process.exit(2); }

const norm = (s) => s.toLowerCase().replace(/[‘’‛′`]/g, "'").replace(/[“”″]/g, '"')
  .replace(/[‐-―−]/g, "-").replace(/\s+/g, " ").trim();
const items = readFileSync(store, "utf8").split("\n").filter(Boolean).map((l) => JSON.parse(l));
const ids = new Set(items.map((i) => i.id));
const bySection = {};
for (const i of items) (bySection[i.section] ??= []).push(norm(i.quote || ""));

const QUOTE = /[“"]([^"“”]{6,}?)[”"]\s*\(((?:S|C)\d{3}|X-[a-z]+)\b[^)]*\)/g;
const FULL = /\[full:\s*([A-Za-z][\w-]*#[a-z]+-\d+)\]/g;
let quotes = 0, refs = 0;
const bad = [];
for (const f of readdirSync(brain).filter((n) => n.endsWith(".md") && n !== "sources.md")) {
  const text = readFileSync(join(brain, f), "utf8");
  for (const m of text.matchAll(QUOTE)) {
    quotes++;
    const q = norm(m[1]), sec = m[2];
    if (q.split(" ").length > 45) bad.push(`${f}: quote over 45 words (${sec})`);
    else if (!(bySection[sec] || []).some((t) => t.includes(q))) bad.push(`${f}: not word for word in ${sec}: "${m[1].slice(0, 60)}"`);
  }
  for (const m of text.matchAll(FULL)) {
    refs++;
    if (!ids.has(m[1])) bad.push(`${f}: [full: ${m[1]}] names no item`);
  }
}
console.log(`checked ${quotes} quotes and ${refs} [full: ...] references against ${items.length} items`);
if (bad.length) { console.log(`${bad.length} problems:`); for (const b of bad) console.log("  " + b); process.exit(1); }
console.log("all quotes word for word, all references resolve");
