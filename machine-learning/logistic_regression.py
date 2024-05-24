import numpy as np

class LogisticRegression:
    def __init__(self, lr: float = 0.0002, n_iters: int = 1000) -> None:
        self.lr = lr 
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            linear_preds = np.dot(X, self.weights) + self.bias
            logits = self._sigmoid(linear_preds)

            dw = 1/n_samples * np.dot(X.T, (logits - y))
            db = 1/n_samples * np.sum((logits - y))

            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db

    @staticmethod
    def _sigmoid(units: np.ndarray):
        return 1/(1+np.exp(-units))

    def predict(self, X):
        linear_preds = np.dot(X, self.weights) + self.bias
        logits = self._sigmoid(linear_preds)
        y_preds = [0 if _y <= 0.5 else 1 for _y in logits]
        return y_preds