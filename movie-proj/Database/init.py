# database/__init__.py

from .connection import get_connection
from .repository import insert_movie, get_movie_by_id, get_all_movies

__all__ = [
    "get_connection",
    "insert_movie",
    "get_movie_by_id",
    "get_all_movies"
]
