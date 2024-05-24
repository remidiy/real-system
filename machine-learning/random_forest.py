from collections import Counter
from typing import List, Optional
import numpy as np
from decision_tree import DecisionTree, TreeNode

class RandomForest:
    def __init__(self, n_trees: int=100, max_depth: int=10, min_sample_split: int = 10, n_features: Optional[int] = None, bootstrapping: int = 10) -> None:
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_sample_split = min_sample_split
        self.n_features = n_features
        self.bootstrapping = bootstrapping
        self.trees: List[DecisionTree] = []

    def fit(self, X: np.ndarray, y: np.ndarray):
        
        for _ in range(self.n_trees):
            tree = DecisionTree(max_depth=self.max_depth,
                                num_features=self.n_features,
                                min_sample_split=self.min_sample_split)
            X_bootstrapped, y_bootstrapped = self._bootstrap(X, y)
            tree.fit(X_bootstrapped, y_bootstrapped)
            self.trees.append(tree)

    def _bootstrap(self, X: np.ndarray, y:  np.ndarray):
        n_samples = X.shape[0]
        indices = np.random.choice(n_samples, self.bootstrapping, replace=True)
        return X[indices], y[indices]
    
    def _most_common_label(self, y: np.ndarray):
        return Counter(y).most_common(1)[0][0]

    def predict(self, X: np.ndarray):
        preds = np.array([preds.append(tree.predict(X)) for tree in self.trees])
        preds = np.swapaxes(preds, 1, 0)
        preds = [self._most_common_label(pred) for pred in preds]
        return np.array(preds)
        
            
            
                

