import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import add_after_panel as m


def test_adds_section_once_and_escapes(tmp_path):
    (tmp_path / "after-hearing.json").write_text(json.dumps([{"flag": "F4", "topic": "A & B", "text": "7,245 <x>", "source": "p324"}]))
    (tmp_path / "report.html").write_text('<a href="#exhibits">Exhibits</a><section id="exhibits">E</section>')
    m.main(tmp_path)
    m.main(tmp_path)
    page = (tmp_path / "report.html").read_text()
    assert page.count('id="after"') == 1
    assert "A &amp; B" in page and "7,245 &lt;x&gt;" in page
    assert page.index('id="after"') < page.index('id="exhibits"')
    assert 'href="#after"' in page
