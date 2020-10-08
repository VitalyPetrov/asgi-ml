from typing import Dict, List, Any
from sklearn.datasets import load_iris
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, train_test_split


class ForestIrisClassifier:
    def __init__(self):
        self.features, self.target = load_iris(return_X_y=True)
        self.model: RandomForestClassifier = None

        # TODO: replace with reading from a config
        self._train(
            params_grid={
                "n_estimators": [150],
                "max_depth": range(25, 30),
                "min_samples_leaf": range(5, 10),
                "criterion": ["gini", "entropy"],
            }
        )

    def _train(self, params_grid: Dict[str, List]) -> None:
        self._split_data()
        self.fit(params_grid)

    def _split_data(self) -> None:
        (
            self.features_train,
            self.features_test,
            self.target_train,
            self.target_test,
        ) = train_test_split(
            self.features, self.target, stratify=self.target, test_size=0.2
        )

    def fit(self, params_grid: Dict[str, List]) -> None:
        self.model = RandomForestClassifier(class_weight="balanced")

        estimators = GridSearchCV(
            estimator=self.model, param_grid=params_grid, cv=5, n_jobs=-1
        )

        estimators.fit(self.features_train, self.target_train)
        self.model = estimators.best_estimator_

    def predict(self, features: Dict[str, Any]) -> int:
        return self.model.predict(list(features.values()))
