# src/hn_crawler/application/filters.py
"""Funciones puras que implementan las reglas solicitadas."""

from collections.abc import Iterable

from hn_crawler.domain.models import Entry


def long_titles(entries: Iterable[Entry]) -> list[Entry]:
    """>5 palabras, orden descendente por nº de comentarios."""
    return sorted(
        (e for e in entries if e.word_count > 5),
        key=lambda e: e.comments,
        reverse=True,
    )


def short_titles(entries: Iterable[Entry]) -> list[Entry]:
    """≤5 palabras, orden descendente por puntos."""
    return sorted(
        (e for e in entries if e.word_count <= 5),
        key=lambda e: e.points,
        reverse=True,
    )
