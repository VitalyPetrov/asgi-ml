import pandas as pd
import numpy as np
from sklearn.base import ClassifierMixin
from typing import Any


class ML:
    """
    A wrapper around common scikit-learn classifier

    It may seem to be quite overengineering for scikit-learn classifier.
    It is so :). In fact its used mostly as a demo for more comples
    model serving
    """

    def __init__(
        self, model: ClassifierMixin, model_params: dict[str, Any] = {}
    ) -> None:
        self._model_params = model_params
        self.model: ClassifierMixin = model(**self._model_params)

    def train(
        self, features_train: pd.DataFrame, target_train: pd.Series
    ) -> None:
        self.model.fit(X=features_train, y=target_train)

    def predict_single(
        self, features: np.ndarray | list[float] | pd.DataFrame
    ) -> list[float]:
        """Predict all classes probabilies for single sample"""
        # reshape the given features into 2d array
        f = np.array(features).reshape(1, -1)
        #
        return self.model.predict_proba(f)[0].tolist()
