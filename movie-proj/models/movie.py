from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
from exceptions.exception import ValidationError

@dataclass
class MovieData:
    """Movie data model using dataclass"""
    id: Optional[int]             # Database ID (None when new)
    imdb_id: str                  # IMDb identifier (e.g., "tt3896198")
    title: str                    # Movie title
    year: int                     # Release year
    rating: float                 # Movie rating (e.g., OMDb IMDb rating)
    timestamp: str                # When the record was created/updated

    def to_dict(self) -> dict:
        """Convert dataclass to dictionary"""
        return asdict(self)

    @classmethod
    def from_api_response(cls, api_data: dict) -> 'MovieData':
        """
        Create MovieData from OMDb API response.
        Expects api_data to contain: imdbID, Title, Year, imdbRating
        """
        try:
            return cls(
                id=None,
                imdb_id=api_data['imdbID'],
                title=api_data['Title'],
                year=int(api_data['Year']),
                rating=float(api_data['imdbRating']),
                timestamp=datetime.now().isoformat()
            )
        except KeyError as e:
            raise ValidationError(f"Invalid API response structure: missing {e}")
        except ValueError as e:
            raise ValidationError(f"Invalid value in API response: {e}")
