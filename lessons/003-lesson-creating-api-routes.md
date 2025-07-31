# Lesson 3: Creating API Routes with FastAPI

In our previous lessons, we designed our database schema and created Pydantic models to represent our data in Python. Now, it's time to create the API endpoints that will allow users (or other applications) to interact with our expense tracker.

## What are API Routes?

Think of API routes (or endpoints) as different URLs that our application responds to. Each route is associated with a specific action, like creating a new expense or retrieving a list of existing ones.

For example:
- A `GET` request to `/expenses` could fetch all expenses.
- A `POST` request to `/expenses` could add a new expense.

FastAPI makes it very easy to create these routes using "decorators."

## FastAPI Decorators & Your Code

A decorator in Python is a special function that adds functionality to another function. FastAPI uses decorators like `@router.get()` or `@router.post()` to turn a regular Python function into an API endpoint.

Your `app/routes/expense.py` file is a perfect example of this in action. Let's break down your `list_expenses` route:

```python
from typing import List
from fastapi import APIRouter, HTTPException, status

from app.models.expense import Expense, ExpenseCreate
from app.database import db

router = APIRouter(prefix="/expenses", tags=["expenses"])

# ... (create_expense route is here)

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
```

### Key Parts Explained:

1.  **`router = APIRouter(...)`**: You've created an `APIRouter`. The `prefix` automatically adds `/expenses` to all routes in this file, and `tags` helps group them in the automatic API documentation.
2.  **`@router.get("/")`**: This decorator tells FastAPI that the `list_expenses` function should handle `GET` requests made to the `/expenses/` URL.
3.  **`async def list_expenses()`**: You've correctly made this an `async` function. This is important because you're using an `async` database driver, which allows your application to handle other tasks while waiting for the database query to finish.
4.  **`query = "..."`**: You've defined the exact SQL query to run. This gives you full control over what happens in the database.
5.  **`await db.fetch(query)`**: This is where the magic happens. Your code sends the query to the database and `await`s the result without blocking the whole application. The `db` object comes from your `app/database.py` file.

Your setup is fantastic. Now, let's talk about how to fetch a *single* item.
