import aiocache
from fastapi import Request, FastAPI
from starlette.datastructures import State

from src.conf import settings, MLSettings
from src.ml.forest import ForestIrisClassifier
from src.datamodels.forest import (
    IrisFeatures,
    IrisClassificationResponse,
    IrisLabelProbability,
)


aiocache.caches.add(
    "asgi-ml",
    {
        "cache": "aiocache.RedisCache",
        "timeout": None,
        "endpoint": settings.redis.host,
        "port": settings.redis.port,
        "password": settings.redis.password,
        "db": settings.redis.db,
        "serializer": {
            "class": "aiocache.serializers.MsgPackSerializer",
            "encoding": None,
        },
    },
)


def get_ml(request: Request):
    return request.app.state.ml


def on_startup(app: FastAPI):
    config: MLSettings = app.state.settings.ml
    # TODO: replace in-container training with reading trained instance
    model_params = {
        "n_estimators": config.num_trees,
        "max_depth": config.max_depth,
        "min_samples_leaf": config.samples_leaf,
        "criterion": config.loss_function,
        "test_size": config.test_size,
    }
    app.state.ml = ML(model_params)


def on_shutdown(app: FastAPI):
    app.state.ml = None


class ML(State):
    def __init__(self, model_params):
        super().__init__()
        test_size = model_params.pop("test_size")
        self.model = ForestIrisClassifier(
            test_size=test_size, hyperparams=model_params
        )

    def classify(self, features: IrisFeatures):
        scores = self.model.predict(features.get_2d_representation(features))

        response = []
        for idx, score in enumerate(scores):
            label_probability = IrisLabelProbability(id=idx, probability=score)
            response.append(
                IrisClassificationResponse(label_probability=label_probability)
            )

        return response
