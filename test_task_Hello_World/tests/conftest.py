import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client():
    """Provide a TestClient for the FastAPI application."""
    return TestClient(app)


@pytest.fixture
def sample_task_id():
    """Provide a sample task ID for testing."""
    return 42
