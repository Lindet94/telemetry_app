"""
Exercise: Fetch a single expense by its ID.

Instructions:
1.  This file contains a new route to get a single expense.
2.  Your task is to complete the SQL query.
3.  The query should select an expense from the 'expenses' table where the 'id' matches the `expense_id` provided to the function.
4.  Once you've written the query, you can copy this new route into your `app/routes/expense.py` file to test it out.
"""
from fastapi import APIRouter, HTTPException, status

from app.models.expense import Expense
from app.database import db

# This would be the same router from your expense.py file
router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.get("/{expense_id}", response_model=Expense)
async def get_expense(expense_id: int):
    """Get a single expense by its ID."""
    # HINT: In SQL, how do you filter rows based on a column's value?
    # HINT: Your database driver uses $1, $2, etc. for parameters.
    query = """
    SELECT id, amount, vendor, category, description, created_at, updated_at
    FROM expenses
    WHERE -- YOUR CODE HERE
    """
    try:
        result = await db.fetchrow(query, expense_id)
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Expense with ID {expense_id} not found"
            )
        return result
    except Exception as e:
        # This is a general catch-all. In a real app, you might want
        # to handle specific database errors differently.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching expense: {str(e)}",
        ) from e
