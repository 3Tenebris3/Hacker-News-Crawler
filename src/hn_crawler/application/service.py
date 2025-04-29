# src/hn_crawler/application/service.py
"""
Caso de uso principal: entregar los datos ya filtrados.
El decorador `lru_cache` evita múltiples scrapes dentro de un mismo proceso.
"""

from functools import lru_cache
from typing import Literal

from hn_crawler.application import filters
from hn_crawler.infra.scraper import HackerNewsScraper

FilterName = Literal["long", "short", None]


@lru_cache(maxsize=1)
def _cached_entries() -> tuple[tuple[int, ...], ...]:
    """Memoriza el scrape; devuelve tupla de tuplas (hashable para caché)."""
    scraper = HackerNewsScraper()
    return tuple(scraper.fetch())  # type: ignore[arg-type]


def list_entries(filter_name: FilterName = None):
    data = _cached_entries()
    match filter_name:
        case "long":
            return filters.long_titles(data)
        case "short":
            return filters.short_titles(data)
        case _:
            return data
