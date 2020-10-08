from fastapi import Request
from starlette.datastructures import State
from typing import Dict, Any

from ..conf import Settings
from ..ml.forest import ForestIrisClassifier


def get_ml(request: Request):
    return request.app.state.ml


def load(app, config: Settings):
    # TODO: replace in-container training with reading trained instance
    kwargs = {
        "n_estimators": config.ml.num_trees,
        "max_depth": config.ml.max_depth,
        "min_samples_leaf": config.ml.samples_leaf,
        "criterion": config.ml.loss_function,
        "test_size": config.ml.test_size
    }
    app.state.ml = ForestIrisClassifier(**kwargs)


class ML(State):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = ForestIrisClassifier(**kwargs)

    def classify(self, features: Dict[str, Any]):
        pass
