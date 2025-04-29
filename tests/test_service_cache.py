# Removed unused import: importlib
from hn_crawler.application import service


def test_scraper_called_only_once(mocker):
    # ▸ Asegurarnos de partir SIN entradas en caché
    service._cached_entries.cache_clear()

    mock = mocker.patch(
        "hn_crawler.infra.scraper.HackerNewsScraper.fetch",
        return_value=[],
    )

    # primer llamado — llena caché y usa el mock
    service.list_entries()
    # segundo llamado — sale del cache ⇒ fetch NO vuelve a ejecutarse
    service.list_entries("long")

    assert mock.call_count == 1
