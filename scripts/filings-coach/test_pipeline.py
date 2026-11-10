"""Small tests for the parts that decide what counts as evidence. Standard library only.

    cd scripts/filings-coach && python3 -m unittest test_pipeline -v
"""
import json
import os
import tempfile
import unittest
from pathlib import Path

# Point every path at a throwaway folder BEFORE the pipeline modules are imported.
TMP = Path(tempfile.mkdtemp())
os.environ["FC_BUILD"] = str(TMP / "build")
os.environ["FC_SOIC"] = str(TMP / "soic")

import registry  # noqa: E402
import verify  # noqa: E402


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


class BookQuoteCheck(unittest.TestCase):
    def setUp(self):
        write(TMP / "build/books/md/doc-a/p003.txt", "Cash flow from\noperations   lagged profit for years.")

    def test_quote_matches_across_line_breaks_and_spaces(self):
        row = {"source": "doc-a", "cite": "p.3", "quote": "Cash flow from operations lagged profit"}
        self.assertEqual(verify.check_book(row), "ok")

    def test_quote_on_wrong_page_fails(self):
        row = {"source": "doc-a", "cite": "p.4", "quote": "Cash flow from operations"}
        self.assertEqual(verify.check_book(row), "no-page")

    def test_altered_quote_fails(self):
        row = {"source": "doc-a", "cite": "p.3", "quote": "Cash flow from operations beat profit"}
        self.assertEqual(verify.check_book(row), "FAIL")

    def test_quote_over_25_words_is_refused(self):
        row = {"source": "doc-a", "cite": "p.3", "quote": " ".join(["word"] * 26)}
        self.assertEqual(verify.check_book(row), "quote-too-long")


class SoicCiteCheck(unittest.TestCase):
    def setUp(self):
        write(TMP / "soic/concepts/note-x.md", "Receivables bloat (SOICC2 00:04:51-00:05:15) and more.")

    def test_cite_present_in_note(self):
        self.assertEqual(verify.check_soic({"source": "note-x", "cite": "SOICC2 00:04:51-00:05:15"}), "ok")

    def test_invented_timestamp_fails(self):
        self.assertEqual(verify.check_soic({"source": "note-x", "cite": "SOICC2 00:09:00"}), "FAIL")

    def test_wrong_ref_code_fails(self):
        self.assertEqual(verify.check_soic({"source": "note-x", "cite": "MODULC 00:04:51"}), "FAIL")

    def test_no_ref_is_marked_not_failed(self):
        self.assertEqual(verify.check_soic({"source": "note-x", "cite": "no-ref"}), "no-ref")


class ChangeDetection(unittest.TestCase):
    def test_new_changed_removed(self):
        before = {"a": {"sha256": "1"}, "b": {"sha256": "2"}, "gone": {"sha256": "3"}}
        now = {"a": {"sha256": "1"}, "b": {"sha256": "9"}, "fresh": {"sha256": "4"}}
        new, changed, removed, unchanged = registry.compare(now, before)
        self.assertEqual((new, changed, removed, unchanged), (["fresh"], ["b"], ["gone"], ["a"]))

    def test_folder_fingerprint_changes_when_a_page_changes(self):
        folder = TMP / "fp"
        write(folder / "p001.txt", "one")
        first = registry.fingerprint_folder(folder)
        write(folder / "p001.txt", "one, edited")
        self.assertNotEqual(first, registry.fingerprint_folder(folder))

    def test_plan_lists_only_new_and_changed(self):
        write(TMP / "soic/topics/t1.md", "topic")
        write(TMP / "build/books/manifest.jsonl", json.dumps({"id": "doc-a", "status": "ok"}) + "\n")
        registry.cmd_record()                       # everything on disk is now "read"
        write(TMP / "soic/topics/t2.md", "a new topic")
        registry.cmd_plan()
        planned = (TMP / "build/pending/soic-1.txt").read_text()
        self.assertIn("t2.md", planned)
        self.assertNotIn("t1.md", planned)


if __name__ == "__main__":
    unittest.main()
