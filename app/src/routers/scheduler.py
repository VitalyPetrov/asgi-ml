from datetime import datetime
from fastapi import APIRouter, Depends
from celery import Celery
from celery.result import AsyncResult

from src.datamodels.task import Task, TaskResult
from src.dependencies.celery import get_celery

router = APIRouter()


@router.post(
    "/task",
    tags=["main"],
    description="Create and schedule computational-intenstive task",
    response_model=Task,
)
async def create_task(
    x: float,
    y: float,
    celery_worker: Celery = Depends(get_celery),
) -> Task:
    task = celery_worker.send_task("dummy", (x, y))
    return Task(task_id=task.id, dtm=datetime.now())


@router.get(
    "/task/{task_id}",
    tags=["main"],
    description="Get result of already done task",
    response_model=TaskResult,
)
async def get_task_result(
    task_id: str, celery_worker: Celery = Depends(get_celery)
) -> TaskResult:
    task = AsyncResult(task_id, app=celery_worker)

    if not task.ready():
        return TaskResult()

    return TaskResult(done=True, result=task.get())
