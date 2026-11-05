from fastapi import FastAPI, HTTPException

from app.core.config import APP_NAME
from app.database.connection import check_database_connection

app = FastAPI(
    title=APP_NAME,
    description="Real-Time Intelligent Public Transport Tracking System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to BusTrack AI Backend",
        "status": "running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "application": APP_NAME
    }


@app.get("/api/db-check")
def database_check():
    if check_database_connection():
        return {
            "status": "success",
            "database": "bustrack_aiii",
            "message": "MySQL connection successful"
        }

    raise HTTPException(
        status_code=503,
        detail="MySQL database connection failed"
    )