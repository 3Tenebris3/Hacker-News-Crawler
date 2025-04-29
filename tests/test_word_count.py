from hn_crawler.domain.models import Entry


def test_word_count_property():
    entry = Entry(1, "This is - a self-explained example", 0, 0)
    assert entry.word_count == 5
