import numpy as np

class NaiveBayes:
    def fit(self, X: np.ndarray, y: np.ndarray):
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(self._classes)

        # caclulate mean, variance, priors
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self._priors = np.zeros(n_classes, dtype=np.float64)

        for idx, cls in enumerate(self._classes):
            X_cls = X[y == cls]
            self._mean[idx, :] = X_cls.mean(axis=0)
            self._var[idx, :] = X_cls.var(axis=0)
            self._priors[idx] = X_cls.shape[0]/float(n_samples)

    def predict(self, X):
        y_pred = [self._predict(x) for x in X]
        return y_pred

    def _gasussian(self, idx, x):
        pass

    def _predict(self, x):
        posteriors = []

        for idx in range(len(self._classes)):
            prior = np.log(self._priors[idx])
            posterior = np.sum(np.log(self._gasussian(idx, x)))
            posteriors.append(posterior + prior)

        return self._classes[np.argmax(posteriors)]