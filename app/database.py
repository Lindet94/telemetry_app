"""Database session management."""

from typing import Any, List, Optional

import asyncpg
from asyncpg import Record


class Database:
    """Database connection pool manager for asyncpg.

    Manages a connection pool to PostgreSQL database using asyncpg.
    Provides methods for executing queries and fetching results.
    """

    def __init__(self):
        """Initialize the Database instance with no active connection pool."""
        self.pool: Optional[asyncpg.Pool] = None

    async def connect(self, dsn: str) -> None:
        """Establish a connection pool to the PostgreSQL database.

        Args:
            dsn: Database connection string in the format:
                 postgresql://user:password@host:port/database

        Raises:
            RuntimeError: If the connection pool creation fails.
        """
        self.pool = await asyncpg.create_pool(dsn)
        if self.pool is None:
            raise RuntimeError("Failed to create database connection pool")

    async def close(self) -> None:
        """Close the database connection pool and release all connections.

        This method is idempotent and safe to call multiple times.
        """
        if self.pool is not None:
            await self.pool.close()
            self.pool = None

    async def execute(self, query: str, *args: Any) -> str:
        """Execute a SQL query that doesn't return data (INSERT, UPDATE, DELETE).

        Args:
            query: SQL query string with optional placeholders ($1, $2, etc.).
            *args: Values to substitute for placeholders in the query.

        Returns:
            Status string from the database (e.g., "INSERT 0 1", "UPDATE 5").

        Raises:
            RuntimeError: If the database connection is not established.
            asyncpg.PostgresError: If the query execution fails.
        """
        if self.pool is None:
            raise RuntimeError("Database connection is not established")
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def fetch(self, query: str, *args: Any) -> List[Record]:
        """Execute a SQL query and fetch all result rows.

        Args:
            query: SQL query string with optional placeholders ($1, $2, etc.).
            *args: Values to substitute for placeholders in the query.

        Returns:
            List of Record objects representing the query results.
            Returns an empty list if no rows match.

        Raises:
            RuntimeError: If the database connection is not established.
            asyncpg.PostgresError: If the query execution fails.
        """
        if self.pool is None:
            raise RuntimeError("Database connection is not established")
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def fetchrow(self, query: str, *args: Any) -> Optional[Record]:
        """Execute a SQL query and fetch a single result row.

        Args:
            query: SQL query string with optional placeholders ($1, $2, etc.).
            *args: Values to substitute for placeholders in the query.

        Returns:
            A Record object if a row is found, None otherwise.

        Raises:
            RuntimeError: If the database connection is not established.
            asyncpg.PostgresError: If the query execution fails.
        """
        if self.pool is None:
            raise RuntimeError("Database connection is not established")
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(query, *args)


db = Database()
