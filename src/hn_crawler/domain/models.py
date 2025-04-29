"""
Entidades de dominio para el crawler de Hacker News.
"""

from dataclasses import dataclass
import re

# acepta guiones dentro de la palabra
_WORD_RE = re.compile(r"\b\w+(?:-\w+)*\b")

@dataclass(frozen=True)
class Entry:
    """
    Representa una entrada de la portada de Hacker News.

    Atributos
    ---------
    rank : int
        Posición en la lista.
    title : str
        Título del enlace.
    points : int
        Puntuación (“karma”) recibida.
    comments : int
        Número de comentarios.
    """

    rank: int
    title: str
    points: int
    comments: int

    # ------------------------------------------------------------------ #
    # Propiedades derivadas
    # ------------------------------------------------------------------ #
    @property
    def word_count(self) -> int:
        """
        Número de palabras del título, ignorando símbolos.

        Ejemplo
        -------
        >>> Entry(1, "This - is a test", 0, 0).word_count
        4
        """
        return len(_WORD_RE.findall(self.title))
