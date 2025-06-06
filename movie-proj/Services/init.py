# services/__init__.py

from .movie_service import (
    add_movie,
    fetch_movie,
    fetch_all_movies,
    modify_movie,
    remove_movie
)

__all__ = [
    "add_movie",
    "fetch_movie",
    "fetch_all_movies",
    "modify_movie",
    "remove_movie"
]
