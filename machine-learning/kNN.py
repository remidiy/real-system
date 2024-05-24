from collections import Counter
from typing import List
import numpy as np

class kNN:
    def __init__(self, k: int, ) -> None:
        self.k = k
    
    def fit(self, X: List[int], y: List[int]):
        self.X = X
        self.y = y

    def predict(self, X: List[int]):
        return [self._predict(x_pred) for x_pred in X]

    def _predict(self, x_pred):
        distances = [self._calc_distance(x_pred, x_train) for x_train in self.X]
        k_indices = np.argsort(distances)[:self.k]
        nn = [self.y[i] for i in k_indices]
        most_common = Counter(nn).most_common()
        return most_common

    @staticmethod
    def _calc_distance(x1, x2):
        return np.sqrt(np.sum((x1-x2)**2))