# ============================================================
# DevOps from Scratch — API Dockerfile
# ============================================================

# 1. Base image
FROM python:3.12-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy dependency file first (better cache usage)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the application code
COPY app/ ./app/

# 6. Expose the port the app runs on
EXPOSE 8000

# 7. Command to run when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]