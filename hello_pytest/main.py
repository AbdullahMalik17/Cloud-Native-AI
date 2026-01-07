from fastapi import FastAPI
from pydantic import BaseModel

class Task_Model(BaseModel):
    id: int
    description: str

app = FastAPI(
    title="Task API",
    description="A simple task management API"
)

@app.get("/")
def read_root(name: str):
    return {"message": f"Task API is running, {name}"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/tasks", response_model=Task_Model)
def create_task(task: Task_Model):
    # In a real app, this would add to a database
    # For now, just return the task as created
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return {"message": f"Task with id {task_id} deleted"}

@app.put("/tasks/{task_id}", response_model=Task_Model)
def update_task(task_id: int, task: Task_Model):
    # In a real app, this would update in a database
    # For now, return the updated task with the correct id
    return Task_Model(id=task_id, description=task.description)

@app.patch("/tasks/{task_id}", response_model=Task_Model)
def update_specific_task(task_id: int, task: Task_Model):
    # In a real app, this would partially update in a database
    # For now, return the updated task with the correct id
    return Task_Model(id=task_id, description=task.description)