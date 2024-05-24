from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def unravel(root):
        res = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.unravel(root)
    
    @staticmethod
    def ravel(nums: List[int]):
        def helper(l, r):
            if l < r: return None
            m = (l + r)//2
            root = TreeNode(nums[m])
            root.left = helper(l, m-1)
            root.right = helper(m+1, r)
            return root
        return helper(0, len(nums)-1)
    
if __name__ == "__main__":
    # s = Solution()
    print(2**2)
