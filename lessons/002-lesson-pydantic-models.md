# 002 - Pydantic Models for Expense Tracker

## Objective
Create Pydantic models to handle data validation and serialization for the Expense Tracker API.

## What are Pydantic Models?
Pydantic models are Python classes that provide:
- Data validation
- Type hints
- Automatic JSON serialization/deserialization
- Schema documentation

## Models We'll Create

### 1. Base Model
```python
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ExpenseBase(BaseModel):
    amount: float
    vendor: str
    category: str
    description: Optional[str] = None
```

### 2. Create Model (for POST requests)
```python
class ExpenseCreate(ExpenseBase):
    pass  # Inherits all fields from ExpenseBase
```

### 3. Response Model (for GET responses)
```python
class Expense(ExpenseBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Allows conversion from ORM objects
```

## Exercise: Implement the Models

1. Create a new file `app/models/expense.py`
2. Implement the three model classes shown above
3. Add proper docstrings to each class
4. Import them in `app/__init__.py`

## Key Points to Remember
- Use `Optional[]` for fields that can be None
- Add `orm_mode = True` for models that will be returned from the database
- Keep your models focused on data validation, not business logic

## Next Steps
After implementing these models, we'll:
1. Create API endpoints to handle CRUD operations
2. Connect the models to our database
3. Add request/response validation

Would you like me to help you with any part of this exercise? Respond with:
- "I need help with the model implementation"
- "I need help with the imports"
- "I've completed the exercise"
