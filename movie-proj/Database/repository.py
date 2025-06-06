from typing import List, Optional
from Database.connection import get_connection
from models.movie import MovieData
from exceptions.exception import DatabaseError

def insert_movie(movie: MovieData) -> int:
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO movies (imdb_id, title, year, rating, timestamp)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id;
                """, (movie.imdb_id, movie.title, movie.year, movie.rating, movie.timestamp))
                new_id = cur.fetchone()["id"]
                conn.commit()
                return new_id
    except Exception as e:
        raise DatabaseError(f"Insert failed: {e}")

def get_movie_by_id(movie_id: int) -> Optional[MovieData]:
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM movies WHERE id = %s;", (movie_id,))
                row = cur.fetchone()
                return MovieData(**row) if row else None
    except Exception as e:
        raise DatabaseError(f"Fetch failed: {e}")

def get_all_movies() -> List[MovieData]:
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM movies;")
                rows = cur.fetchall()
                return [MovieData(**row) for row in rows]
    except Exception as e:
        raise DatabaseError(f"Fetch all failed: {e}")
