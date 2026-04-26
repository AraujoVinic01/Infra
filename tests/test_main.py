"""
Tests for the main API endpoints.

Uses FastAPI's TestClient (built on httpx) to send fake HTTP requests
to the application without actually starting a server.
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_root():
    """The root endpoint should return a welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the DevOps from Scratch API!"}


def test_health_check():
    """The /health endpoint should report a healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}