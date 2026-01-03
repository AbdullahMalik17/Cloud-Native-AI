from fastapi import FastAPI

app = FastAPI(title="Task API")

@app.get("/")
def read_root():
    return {"message": "Task API is running", "version": "1.0.0"}

@app.get("/tasks/{task_id}")
def read_task(task_id: int, details: bool = False):
    task = {
        "id": task_id,
        "title": f"Task {task_id}",
        "status": "pending"
    }
    if details:
        task["description"] = "This is a detailed description"
        task["created_at"] = "2025-01-01T00:00:00Z"
    return task