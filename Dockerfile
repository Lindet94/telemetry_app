# Use a single stage build to simplify file copying
FROM python:3.11-slim

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8000

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create migrations directory and copy migration files
RUN mkdir -p /app/migrations
COPY migrations/ /app/migrations/

# Copy the rest of the application
COPY . .

# Set execute permissions on the migration script
RUN chmod +x /app/migrations/run_migrations.py

# Expose the port the app runs on
EXPOSE $PORT

# Command to run the application
CMD ["sh", "-c", "cd /app && python -m migrations.run_migrations && uvicorn app.main:app --host 0.0.0.0 --port 8000"]