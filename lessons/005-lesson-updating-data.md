# Lesson 5: Updating Data with PUT

Great work building the read operations! The next logical step in a full-featured API is allowing users to modify existing data. In the world of REST APIs, the standard way to update an existing resource is by using the `PUT` HTTP method.

## The `PUT` Method

A `PUT` request is used to fully replace a resource at a specific URL. If the resource doesn't exist, `PUT` can optionally create it, but we'll focus on updating for now.

Just like `@router.post()` and `@router.get()`, FastAPI provides a decorator for `PUT` requests:

```python
@router.put("/expenses/{expense_id}", response_model=Expense)
async def update_expense(expense_id: int, expense: ExpenseCreate):
    # ... logic to update the expense ...
```

Notice a few key things:
1.  **`@router.put(...)`**: The decorator for handling PUT requests.
2.  **`"/expenses/{expense_id}"`**: We use a path parameter to specify *which* expense to update. This is the same pattern we used for fetching a single expense.
3.  **`expense: ExpenseCreate`**: We also accept a request body containing the new data for the expense. We can reuse our `ExpenseCreate` model for this.

## The SQL `UPDATE` Statement

Inside our function, we'll need to execute an `UPDATE` SQL query. The basic syntax looks like this:

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

For our `expenses` table, we'll want to update all the fields based on the incoming data and use the `expense_id` in the `WHERE` clause to target the correct record. We also want to return the updated record, so we'll use the `RETURNING` clause again.

```sql
UPDATE expenses
SET amount = $1, vendor = $2, category = $3, description = $4
WHERE id = $5
RETURNING id, amount, vendor, category, description, created_at, updated_at;
```

Now, let's put it all together in an exercise.
