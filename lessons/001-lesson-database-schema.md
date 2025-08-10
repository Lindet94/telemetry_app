# 001 - Database Schema Design for Expense Tracker

## Objective
Design and implement a PostgreSQL database schema for tracking personal expenses.

## Schema Design

### Expenses Table
```sql
CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    amount DECIMAL(10, 2) NOT NULL,
    vendor VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### Fields Explanation
- `id`: Auto-incrementing primary key
- `amount`: The cost of the expense (supports 2 decimal places)
- `vendor`: Where the expense was made (e.g., "Grocery Store", "Amazon")
- `category`: Category of the expense (e.g., "Food", "Transportation", "Bills")
- `description`: Optional details about the expense
- `created_at`: When the expense was recorded (auto-set)
- `updated_at`: When the expense was last modified (auto-updated)

## Exercise 1: Create a Database Migration

1. Create a new directory called `migrations` in your project root
2. Inside it, create a file named `001_initial_schema.sql` with the table creation SQL above
3. Add a README.md in the migrations directory explaining how to apply migrations

Would you like me to help you with any part of this exercise? Respond with:
- "I need help with the migration file"
- "I need help with the README"
- "I've completed the exercise"

When you're ready, we'll move on to creating the Pydantic models for our API!
