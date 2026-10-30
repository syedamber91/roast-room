import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("bq", Path(__file__).parent / "build_qa_states_file.py")
bq = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bq)

ROWS = [
    {"held": "2024-05-16", "pair": "2", "analyst": "Ana", "asked": "net debt\ntarget", "state": "declined", "evidence": "We will not give a number.", "problems": ""},
    {"held": "2024-05-16", "pair": "1", "analyst": "Ben", "asked": "margin outlook", "state": "answered", "evidence": "About 20 percent.", "problems": ""},
    {"held": "2024-05-16", "pair": "3", "analyst": "Cy", "asked": "update?", "state": "no answer turn", "evidence": "", "problems": ""},
]


def test_only_not_fully_answered_items_are_copied_with_both_sides_cited_and_the_rest_counted():
    text = bq.render(ROWS, {"2024-05-16": "S006"}, "abc", "checked")
    assert 'declined · pair 2 · Ana asked: "net debt target" (S006, analyst question) · management: "We will not give a number." (S006, management answer)' in text
    assert "margin outlook" not in text and "| 2024-05-16 | S006 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |" in text
