# Exercise 6: Implement the Update Expense Endpoint
#
# Your task is to complete the `update_expense` function below.
# This function should handle a PUT request to `/expenses/{expense_id}`.
#
# Requirements:
# 1. Use the `@router.put` decorator.
# 2. The path should be "/{expense_id}".
# 3. It should take in the `expense_id` from the path and an `expense` object from the request body.
# 4. Construct and execute an SQL `UPDATE` query.
# 5. The query should update the `amount`, `vendor`, `category`, and `description` fields.
# 6. Use a `WHERE` clause to target the correct expense by its ID.
# 7. Use the `RETURNING` clause to get the updated record back from the database.
# 8. If no record is found to update, raise a 404 Not Found HTTPException.
# 9. Return the updated expense record as a dictionary.

from fastapi import APIRouter, HTTPException, status
from app.models.expense import Expense, ExpenseCreate
from app.db import db

router = APIRouter()

# Your code goes here!
# @router.put(...)
# async def update_expense(...):
#     query = """
#     UPDATE expenses
#     SET ...
#     WHERE ...
#     RETURNING ...
#     """
#     try:
#         result = await db.fetchrow(
#             query,
#             # ... your parameters here
#         )
#         if not result:
#             # Raise 404
#         return dict(result)
#     except Exception as e:
#         # Raise 500
