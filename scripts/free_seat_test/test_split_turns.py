"""Tests for split_turns.py. Run: python3 -I -m unittest test_split_turns -v   (from this folder)"""
import unittest
from split_turns import split_call

CALL = """Speakers and Participants
Dr. Kiran Mazumdar-Shaw – Executive Chairperson, Biocon Limited
Mr. Saurabh Paliwal – Head - Investor Relations, Biocon Limited
Biocon Limited Q1 Earnings Conference Call Transcript
Moderator: Welcome to the call. After the remarks there is a question-and-answer session.
Saurabh Paliwal: Thanks. Over to Kiran.
Kiran Mazumdar Shaw: We start with results.
Europe: We grew ten percent in Europe.
Key highlights include: debt fell.
Moderator: We will now begin the question-and-answer session.
Jane Analyst: How is debt?
Kiran Mazumdar Shaw: Debt is falling.
"""

class SplitTurns(unittest.TestCase):
    def setUp(self):
        self.roster, self.turns = split_call(CALL)
        self.mgmt = [t for t in self.turns if t["management"]]

    def test_scripted_headings_stay_inside_the_management_turn(self):
        self.assertEqual(len(self.mgmt), 2)
        self.assertIn("We grew ten percent in Europe", self.mgmt[0]["text"])
        self.assertIn("debt fell", self.mgmt[0]["text"])

    def test_investor_relations_host_is_not_management(self):
        self.assertFalse(any(t["label"].startswith("Saurabh") and t["management"] for t in self.turns))

    def test_analyst_after_qa_start_is_a_separate_non_management_turn(self):
        analyst = [t for t in self.turns if t["label"] == "Jane Analyst"]
        self.assertEqual(len(analyst), 1)
        self.assertFalse(analyst[0]["management"])
        self.assertNotIn("Debt is falling", analyst[0]["text"])

if __name__ == "__main__":
    unittest.main()
