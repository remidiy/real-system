import enum
from turtle import distance
import numpy as np

class KMeans:
    def __init__(self, k: int = 5, max_iters: int = 100) -> None:
        self.k = k
        self.max_iters = max_iters 
        self.clusters = [[] for _ in range(k)]
        self.centroids = []

    def predict(self, X):
        self.n_samples, self.n_features = X.shape
        rand_idx = np.random.choice(range(self.n_samples), self.k, replace=False)
        self.centroids = [self.n_samples[idx] for idx in rand_idx]

        for _ in range(self.max_iters):
            self.clusters = self._create_clusters(self.centroids, X)
            centroid_old = self.centroids
            self.centroids = self._get_cendroids(self.clusters)
            if self._converged(centroid_old, self.centroids):
                break

        return self._cluster_labels(self.clusters)
    
    def _cluster_labels(self, clusters):
        labels = np.empty(self.n_samples)
        for cluster_idx, cluster in enumerate(clusters):
            for sample_idx in cluster:
                labels[sample_idx] = cluster_idx

    def _create_clusters(self, centroids, X):
        clusters = [[] for _ in range(self.k)]
        for idx, sample in enumerate(X):
            centroid_idx = self._closest_centroid(sample, centroids)
            clusters[centroid_idx].append(idx)

    def _closest_centroid(self, sample, centroids):
        distances = [self._distance(sample, point) for point in centroids]
        return np.argmin(distances)
    
    def _distance(self, x, y):
        return np.sqrt(np.sum((x-y)**2))

    def _get_cendroids(self, clusters):
        centroids = np.zeros(self.k, self.n_features)
        for cluster_idx, cluster in enumerate(clusters):
            cluster_means = np.mean(cluster, axis=0)
            centroids[cluster_idx] = cluster_means
        return centroids

    def _converged(self, old, new):
        distances = [self._distance(x, y) for x,y in zip(old, new)]
        return sum(distances) == 0