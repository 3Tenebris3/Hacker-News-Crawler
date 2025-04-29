"""
Paquete raíz de hn_crawler.
Mantiene solo metadatos para evitar errores en tiempo de import.
"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("hn_crawler")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "0.0.0-dev"

__all__ = ["__version__"]
