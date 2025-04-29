"""
Infrastructure layer: adapters that talk to the outside world.
Expose HackerNewsScraper para que pueda importarse directamente.

Ejemplo:
    from hn_crawler.infrastructure import HackerNewsScraper
"""

from .scraper import HackerNewsScraper  # noqa: F401

__all__ = ["HackerNewsScraper"]
