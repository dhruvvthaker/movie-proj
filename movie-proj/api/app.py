import logging
from fastapi import FastAPI
from api.routes import router  # Adjust import if needed

# Set up logging to write to app.log in the project root
logging.basicConfig(
    filename='../app.log',  # Adjust path if you want logs in a different location
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Example log message
logging.info("FastAPI application started")

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.app:app", host="127.0.0.1", port=8000, reload=True)
