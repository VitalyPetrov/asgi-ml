from datetime import datetime
from pydantic import BaseModel, constr
from typing import Any


class Task(BaseModel):
    task_id: str
    dtm: datetime


class TaskResult(BaseModel):
    done: bool = False
    result: Any | None = None
