from fastapi import FastAPI
import os
from app.database import db

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Replace with your actual database connection string
    dsn = os.getenv("DATABASE_URL", "postgresql://telemetry_user:postgres@localhost:5432/telemetry")
    await db.connect(dsn)

@app.on_event("shutdown")
async def shutdown():
    await db.close()