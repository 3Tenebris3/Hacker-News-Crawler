# tests/test_filters.py
import pytest
from hn_crawler.application.filters import long_titles, short_titles
from hn_crawler.domain.models import Entry

@pytest.fixture
def sample_entries():
    return [
        Entry(1, "Five words only here", 10, 30),   # 5
        Entry(2, "Exactly six words in this title", 15, 50),  # 6
    ]

def test_short_titles(sample_entries):
    res = short_titles(sample_entries)
    assert [e.rank for e in res] == [1]

def test_long_titles(sample_entries):
    res = long_titles(sample_entries)
    assert [e.rank for e in res] == [2]
