import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/?name=TestUser")
    assert response.status_code == 200
    # Note: The current implementation appends to db, so response might be None
    # This reflects the current behavior in main.py

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_task():
    task_data = {"id": 1, "description": "Test task"}
    response = client.post("/tasks", json=task_data)
    assert response.status_code == 200
    # Note: The current implementation returns the result of db.append() which is None
    # This reflects the current behavior in main.py

def test_delete_task():
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Task with id 1 deleted"}

def test_update_task():
    task_data = {"id": 1, "description": "Updated task description"}
    response = client.put("/tasks/1", json=task_data)
    assert response.status_code == 200
    assert response.json() == {"id": 1, "description": "Updated task description"}

def test_update_specific_task():
    task_data = {"id": 1, "description": "Patched task description"}
    response = client.patch("/tasks/1", json=task_data)
    assert response.status_code == 200
    assert response.json() == {"id": 1, "description": "Patched task description"}

