# services/movie_service.py

from typing import List
from models.movie import MovieData
from Database.repository import (
    insert_movie,
    get_movie_by_id,
    get_all_movies,
    update_movie,
    delete_movie
)
from exceptions.exception import DatabaseError

def add_movie(movie: MovieData) -> MovieData:
    try:
        return insert_movie(movie)
    except Exception as e:
        raise DatabaseError(f"Failed to insert movie: {e}")

def fetch_movie(movie_id: int) -> MovieData:
    movie = get_movie_by_id(movie_id)
    if not movie:
        raise DatabaseError(f"Movie with ID {movie_id} not found")
    return movie

def fetch_all_movies() -> List[MovieData]:
    return get_all_movies()

def modify_movie(movie_id: int, updated_data: MovieData) -> MovieData:
    return update_movie(movie_id, updated_data)

def remove_movie(movie_id: int) -> bool:
    return delete_movie(movie_id)
