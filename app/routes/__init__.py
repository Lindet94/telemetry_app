"""API routes package."""
from fastapi import APIRouter

from . import expense

# Create main router
api_router = APIRouter()

# Include all route modules
api_router.include_router(expense.router)
