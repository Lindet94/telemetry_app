"""Database session management."""

from typing import Any, List, Optional

import asyncpg
from asyncpg import Record


class Database:
    def __init__(self):
        self.pool: Optional[asyncpg.Pool] = None

    async def connect(self, dsn: str) -> None:
        self.pool = await asyncpg.create_pool(dsn)
        if self.pool is None:
            raise RuntimeError("Failed to create database connection pool")

    async def close(self) -> None:
        if self.pool is not None:
            await self.pool.close()
            self.pool = None

    async def execute(self, query: str, *args: Any) -> str:
        if self.pool is None:
            raise RuntimeError("Database connection is not established")
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def fetch(self, query: str, *args: Any) -> List[Record]:
        if self.pool is None:
            raise RuntimeError("Database connection is not established")
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def fetchrow(self, query: str, *args: Any) -> Optional[Record]:
        if self.pool is None:
            raise RuntimeError("Database connection is not established")
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(query, *args)


db = Database()
