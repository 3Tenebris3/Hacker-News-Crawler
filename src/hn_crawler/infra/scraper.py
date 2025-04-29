# src/hn_crawler/infra/scraper.py
"""
Capa de infraestructura: conoce la estructura HTML de Hacker News,
pero el resto de la aplicación no necesita saber de `BeautifulSoup`.
"""

from __future__ import annotations

import httpx
from bs4 import BeautifulSoup

from hn_crawler.domain.models import Entry

HN_URL = "https://news.ycombinator.com/"


class HackerNewsScraper:
    """Obtiene y parsea las primeras *n* entradas de Hacker News."""

    def __init__(self, client: httpx.Client | None = None) -> None:
        self._client = client or httpx.Client(timeout=5.0, follow_redirects=True)

    def fetch(self, limit: int = 30) -> list[Entry]:
        """Devuelve hasta *limit* entradas."""
        response = self._client.get(HN_URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        rows = soup.select("tr.athing")[:limit]               # estructura propia de HN

        entries: list[Entry] = []
        for row in rows:
            rank = int(row.select_one(".rank").text.rstrip("."))
            title = row.select_one(".titleline > a").text.strip()

            subtext = row.find_next_sibling("tr").select_one(".subtext")
            points = int(subtext.select_one(".score").text.split()[0]) if subtext.select_one(".score") else 0
            comments_tag = subtext.find_all("a")[-1]
            comments = int(comments_tag.text.split()[0]) if "comment" in comments_tag.text else 0

            entries.append(Entry(rank, title, points, comments))
        return entries
