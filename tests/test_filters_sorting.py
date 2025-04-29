from hn_crawler.application.filters import long_titles, short_titles
from hn_crawler.domain.models import Entry

entries = [
    Entry(1, "Six words in this very title", points=10, comments=2),   # 6
    Entry(2, "Seven words appear in this title now",  points=5,  comments=99),
    Entry(3, "Four word title!",                     points=42, comments=1),   # 4
    Entry(4, "Five word title exactly here",         points=17, comments=3),   # 5
]

def test_long_titles_sorted_by_comments():
    res = long_titles(entries)
    assert [e.rank for e in res] == [2, 1]      # 99 > 2

def test_short_titles_sorted_by_points():
    res = short_titles(entries)
    assert [e.rank for e in res] == [3, 4]      # 42 > 17
