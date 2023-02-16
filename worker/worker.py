import time

from celery import Celery
from conf import settings, logger

# Wait for rabbitmq to be started
time.sleep(15)

app = Celery(
    "tasks",
    broker=settings.rabbitmq.uri,
    backend=settings.redis.dsn,
)


@app.task(name="dummy")
def add(x, y):
    logger.info("Task Add started")
    time.sleep(10)
    logger.info("Task Add done")
    return x + y
