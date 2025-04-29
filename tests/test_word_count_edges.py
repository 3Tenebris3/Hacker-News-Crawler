from hn_crawler.domain.models import Entry

CASES = [
    ("one-shot", 1),                       # guión corto Unicode
    ("One—shot sentence", 3),              # em-dash
    ("  leading and   double  spaces ", 4),
    ("symbols #hashtag 42°", 3),           # símbolos ignorados
]

def test_word_count_edges():
    for title, expected in CASES:
        assert Entry(1, title, 0, 0).word_count == expected
