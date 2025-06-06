# exceptions/exception.py
# Define custom exceptions for the project

class ValidationError(Exception):
    """Exception raised for validation errors."""
    pass

class DatabaseError(Exception):
    """Exception raised for database related errors."""
    pass

class MovieAPIError(Exception):
    """Exception raised for errors related to external movie API."""
    pass

# You can add more custom exceptions as needed
