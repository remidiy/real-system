"""
# Definition for a QuadTree node.

"""

from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def is_leaf(self, grid):
        r = sum([sum(grid[i]) for i in range(len(grid))])
        if r == len(grid)**2: return (1, 1)
        elif r == 0: return (1, 0)
        else: return (0, 1)
    
    def get_grid(self, rs, re, cs, ce, grid):
        print(rs, re, cs, ce)
        n = []
        for r in range(rs, re):
            n.append(grid[r][cs:ce])
        return n

    def construct(self, grid: List[List[int]]) -> 'Node':
        r, m = len(grid), int(len(grid)/2)
        if r == 1:
            return Node(
                isLeaf=1, 
                val=grid[0][0], 
                topLeft=None, 
                topRight=None,
                bottomLeft=None,
                bottomRight=None)
            
        is_leaf, val = self.is_leaf(grid)
        if not is_leaf:
            return Node(
                isLeaf=is_leaf, 
                val=val,
                topLeft=self.construct(self.get_grid(0, m, 0, m, grid)),
                topRight=self.construct(self.get_grid(0, m, m, r, grid)),
                bottomLeft=self.construct(self.get_grid(m, r, 0, m, grid)),
                bottomRight=self.construct(self.get_grid(m, r, m, r, grid))
                )
        else:
            return Node(
                isLeaf=is_leaf, 
                val=val, 
                topLeft=None, 
                topRight=None,
                bottomLeft=None,
                bottomRight=None)
        
if __name__ == "__main__":
    s = Solution()
    print(s.construct([[0,1],[1,0]]))