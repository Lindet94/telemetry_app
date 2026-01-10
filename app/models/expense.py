"""Pydantic models for expense data validation and serialization.

This module defines the data models used for expense tracking,
including base models for validation and database-backed models.
"""

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ExpenseBase(BaseModel):
    """Base model for expenses with common fields.

    Attributes:
        amount: The monetary amount of the expense (positive float).
        vendor: The name of the vendor or merchant.
        category: The expense category (e.g., 'Food', 'Travel', 'Office').
        description: Optional detailed description of the expense.
    """

    amount: float
    vendor: str
    category: str
    description: Optional[str] = None


class ExpenseCreate(ExpenseBase):
    """Model for creating a new expense via API.

    Inherits all fields from ExpenseBase. Used for request validation
    when creating or updating expenses. Does not include database-managed
    fields like id or timestamps.
    """

    pass


class Expense(ExpenseBase):
    """Complete expense model with database-specific fields.

    Extends ExpenseBase with database-managed fields. Used for API responses
    and represents the full state of an expense as stored in the database.

    Attributes:
        id: Unique identifier assigned by the database.
        created_at: Timestamp when the expense was created.
        updated_at: Timestamp when the expense was last modified.
    """

    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        """Pydantic configuration for ORM compatibility.

        Enables the model to work with ORM objects by allowing
        attribute-based initialization (from_attributes=True).
        """

        from_attributes = True
