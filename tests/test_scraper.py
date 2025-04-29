from hn_crawler.infra.scraper import HackerNewsScraper


def test_scraper_parses(_mock_hn):
    scraper = HackerNewsScraper()
    entries = scraper.fetch(limit=3)
    assert len(entries) == 3
