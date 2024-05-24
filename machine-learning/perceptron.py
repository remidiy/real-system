import numpy as np

def step_func(x):
    return np.where(x > 0, 1, 0)

class Perceptron:
    def __init__(self, lr: float = 0.01, n_iters: int = 1000) -> None:
        self.lr = lr
        self.n_iters = n_iters
        self.activation_func = step_func
        self.weights = None
        self.bias = None

    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            for idx, sample in enumerate(X):
                linears_units = np.dot(sample, self.weights) + self.bias
                logits = self.activation_func(linears_units)

                self.weights += self.lr * np.dot(y[idx] - logits) * sample
                self.bias += self.lr * np.dot(y[idx] - logits)

    def predict(self, X):
        linears_units = np.dot(X, self.weights) + self.bias
        logits = self.activation_func(linears_units)
        return logits