from add_method_panel import panel, rows_of

HEARING = """# H

## I5 Cash
### Q1 Lawyer
TO: the convict
QUESTION: Why is cash from operations below profit?
WHY I ASK: S454 cash conversion gate, DECISIVE: yes
IF DEFLECTED: Give the number.

### Q2 Lawyer
TO: the convict
QUESTION: And the date?
WHY I ASK: S052 and S005 auditor check, DECISIVE: no
IF DEFLECTED: Name the document.
"""


def test_every_lawyer_question_is_listed_with_its_sources():
    rows = rows_of(HEARING)
    assert [r["turn"] for r in rows] == ["Q1", "Q2"]
    html = panel(rows)
    assert 'id="method"' in html and '<span class="src">S454</span>' in html and "<b>2</b>questions in the ten issues" in html
    assert "<b>3</b>different SOIC source ids cited" in html


def test_text_is_escaped():
    rows = [{"issue": "I1 x", "key": "I1", "turn": "Q1", "q": "a < b & c", "why": "S001"}]
    assert "a &lt; b &amp; c" in panel(rows)
