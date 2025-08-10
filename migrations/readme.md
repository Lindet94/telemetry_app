# Database Migrations

This directory contains SQL migration files for the Expense Tracker API database schema.

Migrations should be applied in numerical order. For example, run `001_` before `002_`.


Make sure to set your `DATABASE_URL` environment variable before running migrations:
```bash
export DATABASE_URL=postgresql://user:password@localhost:5432/your_database
```


How to apply migrations:

Example:

```bash
psql -U your_username -d your_database -f 001_initial_schema.sql
```
Or using connection string:

```bash
psql $DATABASE_URL -f 001_initial_schema.sql
```


To verify the migrations were applied:
```bash
psql $DATABASE_URL -c "SELECT * FROM schema_migrations;"
```