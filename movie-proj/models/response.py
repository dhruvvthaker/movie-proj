from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class MovieResponse(BaseModel):
    """Movie response model for API endpoints"""
    id: int = Field(
        ...,
        title="Record ID",
        description="Unique identifier for the movie record in the database",
        example=1,
        ge=1
    )
    imdb_id: str = Field(
        ...,
        title="IMDb ID",
        description="Unique identifier for the movie on IMDb",
        example="tt3896198"
    )
    title: str = Field(
        ...,
        title="Movie Title",
        description="Title of the movie",
        example="Guardians of the Galaxy Vol. 2"
    )
    year: int = Field(
        ...,
        title="Release Year",
        description="Year the movie was released",
        example=2017,
        ge=1900,
        le=2100
    )
    rating: float = Field(
        ...,
        title="Movie Rating",
        description="IMDb rating of the movie",
        example=7.6,
        ge=0,
        le=10
    )
    timestamp: str = Field(
        ...,
        title="Record Timestamp",
        description="ISO 8601 formatted timestamp when movie data was recorded",
        example="2024-03-15T14:30:00.000Z"
    )

class MessageResponse(BaseModel):
    """Message response model"""
    message: str = Field(
        ...,
        title="Response Message",
        description="Human-readable message describing the operation result",
        example="Operation completed successfully",
        max_length=500
    )

class ErrorResponse(BaseModel):
    """Error response model"""
    detail: str = Field(
        ...,
        title="Error Detail",
        description="Detailed error message explaining what went wrong",
        example="Movie not found",
        max_length=1000
    )
    error_code: Optional[str] = Field(
        None,
        title="Error Code",
        description="Machine-readable error code for programmatic error handling",
        example="NOT_FOUND"
    )
    timestamp: Optional[datetime] = Field(
        None,
        title="Error Timestamp",
        description="When the error occurred",
        example="2024-03-15T14:30:00.000Z"
    )

class MovieListResponse(BaseModel):
    """List of movies response model"""
    movies: List[MovieResponse] = Field(
        ...,
        title="Movies",
        description="List of movie records"
    )
