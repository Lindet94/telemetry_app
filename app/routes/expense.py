"""Expense-related API routes."""
from typing import List
from fastapi import APIRouter, HTTPException, status

from app.models.expense import Expense, ExpenseCreate
from app.database import db

router = APIRouter(prefix="/expenses", tags=["expenses"])

@router.post("/", response_model=Expense, status_code=status.HTTP_201_CREATED)
async def create_expense(expense: ExpenseCreate):
    """Create a new expense."""
    query = """
    INSERT INTO expenses (amount, vendor, category, description)
    VALUES ($1, $2, $3, $4)
    RETURNING id, amount, vendor, category, description, created_at, updated_at
    """
    try:
        result = await db.fetchrow(
            query,
            expense.amount,
            expense.vendor,
            expense.category,
            expense.description
        )
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating expense: {str(e)}"
        ) from e

@router.get("/", response_model=List[Expense])
async def list_expenses():
    """List all expenses."""
    query = """
    SELECT id, amount, vendor, category, description, created_at, updated_at
    FROM expenses
    ORDER BY created_at DESC
    """
    try:
        return await db.fetch(query)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching expenses: {str(e)}",
        ) from e
