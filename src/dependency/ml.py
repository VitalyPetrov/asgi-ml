from fastapi import Request, FastAPI
from starlette.datastructures import State

from ..conf import MLSettings
from ..ml.forest import ForestIrisClassifier
from ..datamodels.forest import (
    IrisFeatures,
    IrisClassificationResponse,
    IrisLabelProbability,
)


def get_ml(request: Request):
    return request.app.state.ml


def on_startup(app: FastAPI):
    config: MLSettings = app.state.settings.ml
    # TODO: replace in-container training with reading trained instance
    kwargs = {
        "n_estimators": config.num_trees,
        "max_depth": config.max_depth,
        "min_samples_leaf": config.samples_leaf,
        "criterion": config.loss_function,
        "test_size": config.test_size,
    }
    app.state.ml = ML(kwargs)


def on_shutdown(app: FastAPI):
    pass


class ML(State):
    def __init__(self, kwargs):
        super().__init__()
        test_size = kwargs.pop("test_size")
        self.model = ForestIrisClassifier(
            test_size=test_size, hyperparams=kwargs
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
