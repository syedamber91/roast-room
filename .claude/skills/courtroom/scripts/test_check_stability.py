import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("stab", HERE / "check_stability.py")
stab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stab)


def run(position="wait", scores=(1, 1, 1, 1, 1, 1, 1)):
    return {"decision": {"position": {"key": position}, "scores": [{"section": "S%d" % (i + 1), "final": v} for i, v in enumerate(scores)]}}


def test_identical_runs_are_stable():
    assert stab.compare([run(), run(), run()])["stable"]


def test_one_section_off_by_one_point_is_still_stable():
    assert stab.compare([run(), run(scores=(1, 2, 1, 1, 1, 1, 1)), run()])["stable"]


def test_a_different_position_is_not_stable():
    r = stab.compare([run(), run(position="avoid"), run()])
    assert not r["stable"] and "positions differ" in r["reasons"][0]


def test_two_sections_differing_is_not_stable():
    r = stab.compare([run(), run(scores=(2, 2, 1, 1, 1, 1, 1)), run()])
    assert not r["stable"] and "differ in 2 sections" in " ".join(r["reasons"])


def test_one_section_off_by_two_points_is_not_stable():
    r = stab.compare([run(scores=(0, 1, 1, 1, 1, 1, 1)), run(scores=(2, 1, 1, 1, 1, 1, 1)), run(scores=(1, 1, 1, 1, 1, 1, 1))])
    assert not r["stable"] and "by 2 points" in " ".join(r["reasons"])


def test_fewer_than_two_runs_cannot_be_judged_stable():
    assert not stab.compare([run()])["stable"]
