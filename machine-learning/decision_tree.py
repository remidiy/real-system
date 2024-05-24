from __future__ import annotations
from collections import Counter
from typing import Optional
import numpy as np


class TreeNode:
    def __init__(self, feature: str|int = None, thres: str|int = None, left: TreeNode = None, right: TreeNode = None, value: int=None) -> None:
        self.feature = feature
        self.thres = thres
        self.left = left 
        self.right = right
        self.value = value

    def is_leaf_node(self):
        return self.value is not None

class DecisionTree:
    def __init__(self, max_depth: int = 10, num_features: Optional[int] = None, min_sample_split: int = 2) -> None:
        self.root = None
        self.max_depth = max_depth
        self.num_features = num_features
        self.min_sample_split = min_sample_split


    def fit(self, X: np.ndarray, y: np.ndarray):
        self.num_features = X.shape[1] if self.n_features is None else min(X.shape[1], self.num_features)
        self.root = self._grow_tree(X, y, 0)

    def predict(self, X: np.ndarray):
        return np.array(self._traverse(sample, self.root) for sample in X)
    
    def _traverse(self, x: np.ndarray, node: TreeNode):
        if node.is_leaf_node:
            return node.value
        
        if x[node.feature] >= node.thres:
            self._traverse(x, node.left)
        else:
            self._traverse(x, node.right)

    def _grow_tree(self, X: np.ndarray, y: np.ndarray, depth: int): 
        n_samples, n_feats = X.shape
        n_labels = len(np.unique(y))

        # check for the stopping criteria
        if (depth >= self.max_depth or len(n_labels) == 1 or n_samples <= self.min_sample_split):
            leaf_value = self._most_common_label(y)
            return TreeNode(value=leaf_value)
        feat_idxs = np.random.choice(n_feats, self.num_features, replace=False)

        # calc the best split and thres
        best_thres, best_feature = self._best_split(X, y, feat_idxs)

        # recursively call the _grow_tree to build the tree
        left_idxs, right_idxs = self._split(X[: best_feature], best_thres)
        left_tree = self._grow_tree(X[left_idxs, :], y[left_idxs], depth+1)
        right_tree = self._grow_tree(X[right_idxs, :], y[right_idxs], depth+1)
        return TreeNode(feature=best_feature, thres=best_thres, left=left_tree, right=right_tree)
        
    def _most_common_label(self, y: np.ndarray):
        return Counter(y).most_common(1)[0][0]
    
    def _best_split(self, X: np.ndarray, y: np.ndarray, feat_idxs: list):
        best_gain = -1
        split_idx, split_thres = None, None

        for feat_idx in feat_idxs:
            X_col = X[:, feat_idx]
            thresholds = np.unique(X_col)
            for thres in thresholds:
                # calc the information gain for each threshold
                gain = self._information_gain(X_col, y, thres)
                if gain > best_gain:
                    best_gain = gain
                    split_idx = feat_idx
                    split_thres = thres

        return split_thres, split_idx
    
    def _information_gain(self, X_col, y, thres):
        parent_entropy = self._entropy(y)
        left_idx, right_idx = self._split(X_col, thres)

        if len(left_idx) == 0 or len(right_idx) == 0: return 0
        left_entropy = self._entropy(y[left_idx])
        right_entropy = self._entropy(y[right_idx])
        gain = parent_entropy - (len(left_idx)*left_entropy + len(right_idx)*right_entropy)/len(y)
        return gain

    def _split(self, X, thres):
        return np.argwhere(X >= thres), np.argwhere(X < thres)
    def _entropy(self, y):
        hist = np.bincount(y)
        ps = hist / len(y)
        return -np.sum([p * np.log(p) for p in ps])


