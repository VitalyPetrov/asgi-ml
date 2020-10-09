from typing import Dict, List, Any
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


class ForestIrisClassifier:
    def __init__(self, test_size: int, hyperparams: Dict[str, Any]):
        self.features, self.target = load_iris(return_X_y=True)
        self.model: RandomForestClassifier = RandomForestClassifier()

        self._train(test_size=test_size, params_grid=hyperparams)

    def _train(self, test_size: int, params_grid: Dict[str, List]) -> None:
        self._split_data(test_size)
        self._fit(params_grid)

    def _split_data(self, test_size: int) -> None:
        (
            self.features_train,
            self.features_test,
            self.target_train,
            self.target_test,
        ) = train_test_split(
            self.features,
            self.target,
            stratify=self.target,
            test_size=test_size,
        )

    def _fit(self, params_grid: Dict[str, Any]) -> None:
        self.model = RandomForestClassifier(
            class_weight="balanced", **params_grid
        )

        self.model.fit(self.features_train, self.target_train)

    def predict(self, features_2d: List[List[Any]]) -> List:
        return self.model.predict_proba(features_2d)[0]
