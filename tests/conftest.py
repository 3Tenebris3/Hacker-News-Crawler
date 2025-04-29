"""
Fixtures compartidos para los tests.
Mockea la respuesta de news.ycombinator.com y expone alias de compatibilidad.
"""

import pathlib
import pytest
import requests_mock
import httpx

_FIXTURE_DIR = pathlib.Path(__file__).parent / "fixtures"
_FIXTURE_DIR.mkdir(exist_ok=True)

_HTML_PATH = _FIXTURE_DIR / "hn_top.html"


def _download_html() -> str:
    """Descarga la portada de HN solo si el HTML local no existe."""
    resp = httpx.get("https://news.ycombinator.com/", timeout=10)
    resp.raise_for_status()
    _HTML_PATH.write_text(resp.text, encoding="utf-8")
    return resp.text


@pytest.fixture(autouse=True)
def _mock_hn(requests_mock: requests_mock.Mocker):
    """
    Intercepta todas las peticiones a Hacker News y devuelve HTML estático.

    Se ejecuta automáticamente en todos los tests (autouse=True).
    """
    html = _HTML_PATH.read_text(encoding="utf-8") if _HTML_PATH.exists() else _download_html()
    requests_mock.get("https://news.ycombinator.com/", text=html)
    yield


# Alias opcional: permite que tests antiguos pidan `mock_hn_html`
@pytest.fixture
def mock_hn_html(_mock_hn):
    """Alias para compatibilidad con la firma original del test."""
    return True
