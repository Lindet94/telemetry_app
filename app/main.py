"""Main FastAPI application module."""

import logging
import os

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from asyncpg.exceptions import PostgresError
from prometheus_client import make_asgi_app
from app.middleware.metrics import metrics_middleware

from app.database import db
from app.routes import expense

# Add Prometheus metrics endpoint
metrics_app = make_asgi_app()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Telemetry API",
    description="API for handling telemetry data",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.mount("/metrics", metrics_app)

# Include the expense router
app.include_router(expense.router)
# Add metrics middleware
app.middleware("http")(metrics_middleware)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_database_url() -> str:
    """Get the database URL from environment variables with fallback to default.

    Returns:
        str: The database connection string.
    """
    return os.getenv(
        "DATABASE_URL",
        "postgresql://telemetryapp_user:postgres@localhost:5432/telemetry",
    )


@app.on_event("startup")
async def startup() -> None:
    """Initialize database connection on application startup."""
    try:
        dsn = get_database_url()
        logger.info("Connecting to database...")
        await db.connect(dsn)
        logger.info("Successfully connected to database")
    except Exception as e:
        logger.error("Failed to connect to database: %s", e)
        raise


@app.on_event("shutdown")
async def shutdown() -> None:
    """Clean up database connection on application shutdown."""
    try:
        logger.info("Closing database connection...")
        await db.close()
        logger.info("Database connection closed")
    except Exception as e:
        logger.error("Error closing database connection: %s", e)
        raise


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint.

    Returns:
        dict: Status of the API.
    """
    return {"status": "ok"}


# Example of a route that uses the database
@app.get("/items/")
async def get_items():
    """Example endpoint to fetch items from the database.

    Returns:
        dict: List of items or error message.

    Raises:
        HTTPException: If there's an error fetching items from the database
    """
    try:
        # Example query - adjust according to your schema
        items = await db.fetch("SELECT * FROM items LIMIT 10")
        return {"items": [dict(item) for item in items]}
    except PostgresError as e:
        # Log the full error for debugging
        logger.error("Database error fetching items: %s", str(e), exc_info=True)
        # Return a more specific error message
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=(
                f"Database error: {str(e)}"
                if app.debug
                else "An error occurred while fetching items"
            ),
        ) from e
    except Exception as e:
        # Catch any other unexpected errors
        logger.error("Unexpected error fetching items: %s", str(e), exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=(
                f"An unexpected error occurred: {str(e)}"
                if app.debug
                else "An unexpected error occurred"
            ),
        ) from e
