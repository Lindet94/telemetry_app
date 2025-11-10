"""Main application package for the Expense Tracker API."""

from fastapi import FastAPI

# Import models to make them available when the app is imported
from .models.expense import ExpenseBase, ExpenseCreate, Expense

# Create the FastAPI application
app = FastAPI(
    title="Expense Tracker API",
    description="API for tracking personal expenses",
    version="1.0.0",
)


__all__ = ["app", "Expense", "ExpenseBase", "ExpenseCreate"]
