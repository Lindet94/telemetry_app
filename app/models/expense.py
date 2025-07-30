from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ExpenseBase(BaseModel):
    """Base model for expenses
    """
    amount: float
    vendor: str
    category: str
    description: Optional[str] = None


class ExpenseCreate(ExpenseBase):
    """For creating an expense object
    """
    pass


class Expense(ExpenseBase):
    """Expense model with database-specific fields
    """
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        """Orm config
        """
        from_attributes = True