"""
    FastAPI Telegram Bot Package
"""

__version__="1.0.0"
__author__="delkabo"

from .main import app

__all__ = ["app", "settings"]

# Инициализация при импорте пакета
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())

