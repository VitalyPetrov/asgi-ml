import time
from celery import Celery
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

from ml import ML
from conf import settings, logger


# setup ML model to be served
logger.info(f"Model config: ", settings.ml.dict())
model = ML(model=RandomForestClassifier, model_params=settings.ml.dict())
features_train, target_train = load_iris(return_X_y=True)
model.train(features_train, target_train)


app = Celery(
    "tasks",
    broker=settings.rabbitmq.uri,
    backend=settings.redis.dsn,
)


@app.task(name="score-flower")
def score_flower(iris_features):
    logger.info("Scoring: started")
    res = model.predict_single(features=iris_features)
    time.sleep(30)
    logger.info("Scoring: done")

    return res
