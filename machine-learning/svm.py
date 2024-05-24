import numpy as np

class SVM:
    def __init__(self, lr: float = 0.001, lambda_param: float = 0.01, n_iters: int = 1000) -> None:
        self.lr = lr
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        y_ = np.where(y <= 0, -1, 1)

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            for idx, sample in enumerate(X):
                condition = y_[idx] * (np.dot(sample, self.weights) - self.bias) >= 1
                if condition:
                    self.weights -= self.lr * 2 * self.lambda_param * self.weights
                else:
                    self.weights -= self.lr * (2 * self.lambda_param * self.weights - np.dot(sample, y_[idx]))
                    self.bias -= self.lr * y_[idx]

    def predict(self, X: np.ndarray):
        return np.sign(np.dot(X, self.weights) - self.bias)