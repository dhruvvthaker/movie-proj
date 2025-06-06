import psycopg2
from psycopg2.extras import RealDictCursor
from config.settings import settings
from exceptions.exception import DatabaseError

def get_connection():
    try:
        return psycopg2.connect(
            dbname=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            cursor_factory=RealDictCursor
        )
    except Exception as e:
        raise DatabaseError(f"Database connection failed: {e}")
