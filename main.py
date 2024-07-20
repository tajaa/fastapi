from typing import List, Optional
from uuid import UUID, uuid4

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    id: Optional[UUID] = None
    title: str
    description: Optional[str] = None
    completed: bool = False


tasks = []


@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    """creating a task"""
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/tasks/", response_model=List[Task])
def read_tasks():
    """read tasks"""
    return tasks


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
