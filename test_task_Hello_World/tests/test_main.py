import pytest


class TestRootEndpoint:
    """Tests for the root endpoint."""

    def test_read_root_returns_200(self, client):
        """Root endpoint should return 200 status code."""
        response = client.get("/")
        assert response.status_code == 200

    def test_read_root_returns_message(self, client):
        """Root endpoint should return expected message."""
        response = client.get("/")
        data = response.json()
        assert data["message"] == "Task API is running"

    def test_read_root_returns_version(self, client):
        """Root endpoint should include version."""
        response = client.get("/")
        data = response.json()
        assert data["version"] == "1.0.0"


class TestTaskEndpoint:
    """Tests for the task endpoint."""

    def test_read_task_returns_200(self, client, sample_task_id):
        """Task endpoint should return 200 status code."""
        response = client.get(f"/tasks/{sample_task_id}")
        assert response.status_code == 200

    def test_read_task_returns_correct_id(self, client, sample_task_id):
        """Task endpoint should return the requested task ID."""
        response = client.get(f"/tasks/{sample_task_id}")
        data = response.json()
        assert data["id"] == sample_task_id

    def test_read_task_returns_title(self, client, sample_task_id):
        """Task endpoint should return task title."""
        response = client.get(f"/tasks/{sample_task_id}")
        data = response.json()
        assert data["title"] == f"Task {sample_task_id}"

    def test_read_task_returns_status(self, client, sample_task_id):
        """Task endpoint should return pending status."""
        response = client.get(f"/tasks/{sample_task_id}")
        data = response.json()
        assert data["status"] == "pending"

    def test_read_task_without_details(self, client, sample_task_id):
        """Task without details flag should not include description."""
        response = client.get(f"/tasks/{sample_task_id}")
        data = response.json()
        assert "description" not in data
        assert "created_at" not in data

    def test_read_task_with_details(self, client, sample_task_id):
        """Task with details=true should include description and created_at."""
        response = client.get(f"/tasks/{sample_task_id}?details=true")
        data = response.json()
        assert "description" in data
        assert data["description"] == "This is a detailed description"
        assert "created_at" in data
        assert data["created_at"] == "2025-01-01T00:00:00Z"

    @pytest.mark.parametrize("task_id", [1, 100, 999])
    def test_read_task_various_ids(self, client, task_id):
        """Task endpoint should work with various task IDs."""
        response = client.get(f"/tasks/{task_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id

    def test_read_task_invalid_id_type(self, client):
        """Task endpoint should reject non-integer task IDs."""
        response = client.get("/tasks/invalid")
        assert response.status_code == 422  # Validation error
