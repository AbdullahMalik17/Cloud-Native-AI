from fastapi import FastAPI , Depends
from sqlmodel import SQLModel, Field , create_engine, Session, select
import os
from dotenv import load_dotenv , find_dotenv
load_dotenv(find_dotenv())

DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL, echo=True)

# How do we create tables in the neon 
# def create_tables():
#     SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = Field(default=None)

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.post("/tasks")
def create_task(task: Task, session: Session = Depends(get_session)):
    session.add(task)
    session.commit()
    session.refresh(task)
    return {"task": task}

@app.get("/tasks")
def read_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    return {"tasks": tasks}

@app.get("/tasks/{task_id}")
def read_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        return {"error": "Task not found"}
