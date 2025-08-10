#!/usr/bin/env python3
"""
Database migration script for the Expense Tracker API.
Runs the SQL migration from the migrations directory.
"""
import asyncio
import os
import asyncpg
from pathlib import Path

# Get database URL from environment or use default
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://telemetryapp_user:postgres@localhost:5432/telemetry"
)

# Path to the SQL migration file
MIGRATION_FILE = Path(__file__).parent / "011_intital_schema.sql"

async def run_migrations():
    """Run database migrations from the SQL file."""
    print("Running database migrations...")
    
    try:
        # Read the SQL migration file
        if not MIGRATION_FILE.exists():
            raise FileNotFoundError(f"Migration file not found: {MIGRATION_FILE}")
            
        sql = MIGRATION_FILE.read_text()
        
        # Connect to the database
        conn = await asyncpg.connect(DATABASE_URL)
        
        # Execute the SQL from the file
        await conn.execute(sql)
        print("✅ Database migrations completed successfully!")
        
    except Exception as e:
        print(f"❌ Error running migrations: {e}")
        raise
    finally:
        # Close the connection
        if 'conn' in locals():
            await conn.close()

if __name__ == "__main__":
    asyncio.run(run_migrations())
