from fastapi import APIRouter, HTTPException, status
from typing import List
from models.response import MovieResponse, MovieListResponse, MessageResponse, ErrorResponse
from models.movie import MovieData
from Services.movie_service import (
    add_movie,
    fetch_movie,
    fetch_all_movies,
    modify_movie,
    remove_movie
)
from exceptions.exception import DatabaseError, ValidationError

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.get("/", response_model=MovieListResponse)
def get_movies():
    try:
        movies = fetch_all_movies()
        return {"movies": [MovieResponse(**movie.to_dict()) for movie in movies]}
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{movie_id}", response_model=MovieResponse, responses={404: {"model": ErrorResponse}})
def get_movie(movie_id: int):
    try:
        movie = fetch_movie(movie_id)
        return MovieResponse(**movie.to_dict())
    except DatabaseError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=MovieResponse, status_code=status.HTTP_201_CREATED, responses={400: {"model": ErrorResponse}})
def create_movie(movie: MovieResponse):
    try:
        movie_data = MovieData(
            id=None,
            imdb_id=movie.imdb_id,
            title=movie.title,
            year=movie.year,
            rating=movie.rating,
            timestamp=movie.timestamp
        )
        inserted = add_movie(movie_data)
        return MovieResponse(**inserted.to_dict())
    except (DatabaseError, ValidationError) as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.patch("/{movie_id}", response_model=MovieResponse, responses={404: {"model": ErrorResponse}})
def update_movie(movie_id: int, movie: MovieResponse):
    try:
        updated_data = MovieData(
            id=movie_id,
            imdb_id=movie.imdb_id,
            title=movie.title,
            year=movie.year,
            rating=movie.rating,
            timestamp=movie.timestamp
        )
        updated = modify_movie(movie_id, updated_data)
        return MovieResponse(**updated.to_dict())
    except DatabaseError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{movie_id}", response_model=MessageResponse, responses={404: {"model": ErrorResponse}})
def delete_movie(movie_id: int):
    try:
        success = remove_movie(movie_id)
        if not success:
            raise HTTPException(status_code=404, detail="Movie not found")
        return {"message": "Movie deleted successfully"}
    except DatabaseError as e:
        raise HTTPException(status_code=404, detail=str(e))