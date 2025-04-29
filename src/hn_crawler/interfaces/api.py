# src/hn_crawler/interfaces/api.py
from fastapi import APIRouter

from hn_crawler.application.service import list_entries

router = APIRouter(tags=["entries"])


@router.get("/entries")
def entries(filter: str | None = None):
    """Devuelve JSON con las entradas, opcionalmente filtradas."""
    return list_entries(filter)  # FastAPI serializa dataclass → dict
