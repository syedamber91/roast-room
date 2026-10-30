import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
JUDGE = (ROOT / ".claude" / "agents" / "court-judge.md").read_text(encoding="utf-8")
PROMPTS = (HERE.parent / "references" / "hearing-prompts.md").read_text(encoding="utf-8")
ISSUES = json.loads((HERE.parent / "references" / "issues.json").read_text(encoding="utf-8"))


def test_the_judge_agent_is_read_only_and_may_not_open_a_brain():
    front = JUDGE.split("---")[1]
    assert "name: court-judge" in front and "tools: Read, Grep, Glob" in front
    assert "Never open anything under `.claude/skills/roast-room/brains/`" in JUDGE
    assert "may never go higher" in JUDGE.replace("You may never go higher", "may never go higher")
    assert "—" not in JUDGE and "—" not in PROMPTS


def test_every_hearing_turn_and_both_lawyer_and_judge_prompts_say_not_to_read_a_company_brain():
    for turn in ("### Convict opening", "### Lawyer opening", "### Lawyer baseline", "### Convict baseline", "### Judge baseline", "### Q1 Lawyer", "### A1 Convict",
                 "### Judge note", "### WA1 Convict", "### Judge close", "### X1 Lawyer", "### XA1 Convict", "### Convict closing", "### Lawyer closing", "### Judge final"):
        assert turn in PROMPTS, turn
    prompts_by_role = re.split(r"\n### ", PROMPTS)
    for block in prompts_by_role:
        if block.startswith(("Lawyer", "Judge")) or block.startswith("Judge"):
            if "```" in block:
                assert "do not read" in block.lower(), block.splitlines()[0]


def test_the_prompts_cover_the_whole_baseline_and_the_convict_blocks_respect_the_three_file_rule():
    assert "B01 to B26" in PROMPTS and len(ISSUES["baseline"]) == 26
    assert "at most three more files this call" in PROMPTS
    for word in ("answered", "partial", "deflected", "no data", "unverified"):
        assert word in JUDGE
    for move in ("cite", "mitigate", "challenge", "concede", "not in my record"):
        assert move in PROMPTS
