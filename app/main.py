"""
DevOps from Scratch - API Application

A simple FastAPI service used as the foundation of this DevOps portfolio project.
Each endpoint is intentionally minimal so we can focus on the surrounding tooling
(Docker, CI/CD, Kubernetes, monitoring, etc.) in later phases.
"""

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# Create the FastAPI application instance
app = FastAPI(
    title="DevOps from Scratch API",
    description="A learning-oriented API used as the core of a DevOps portfolio project.",
    version="0.3.0",
)

# Setup Prometheus instrumentation: exposes metrics at /metrics
Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    """Welcome endpoint. Returns a friendly message."""
    return {"message": "Welcome to the DevOps from Scratch API!"}


@app.get("/health")
def health_check():
    """
    Health check endpoint.

    Used by orchestration tools (Docker, Kubernetes) to verify the
    application is running and ready to receive traffic.
    """
    return {"status": "healthy"}