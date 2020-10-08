import numpy as np
from typing import Dict, List, Any
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split


class ForestIrisClassifier:
    def __init__(self, hyperparams: Dict[str, Any]):
        self.features, self.target = load_iris(return_X_y=True)
        self.model: RandomForestClassifier = RandomForestClassifier()

        self._train(hyperparams)

    def _train(self, params_grid: Dict[str, List]) -> None:
        self._split_data()
        self._fit(params_grid)

    def _split_data(self) -> None:
        (
            self.features_train,
            self.features_test,
            self.target_train,
            self.target_test,
        ) = train_test_split(
            self.features, self.target, stratify=self.target, test_size=0.2
        )

    def _fit(self, params_grid: Dict[str, List]) -> None:
        self.model = RandomForestClassifier(class_weight="balanced")

        estimators = GridSearchCV(
            estimator=self.model, param_grid=params_grid, cv=5, n_jobs=-1
        )

        estimators.fit(self.features_train, self.target_train)
        self.model = estimators.best_estimator_

    def predict(self, features: Dict[str, Any]) -> int:
        features_2d = [list(features.values())]
        return self.model.predict_proba(features_2d).argmax()
