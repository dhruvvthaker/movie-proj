import logging

# Set up logging to write to app.log in the project root
logging.basicConfig(
    filename='../app.log',  # Adjust path if you want logs in a different location
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Example log message
logging.info("FastAPI application started")
