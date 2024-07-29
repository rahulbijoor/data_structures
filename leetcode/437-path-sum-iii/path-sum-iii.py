# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPath(self, root: Optional[TreeNode], targetSum: int, count: List[int]):
        if not root:
            return
        
        
        
        if targetSum - root.val == 0:
            count[0] += 1
        self.countPath(root.left, targetSum - root.val, count)
        self.countPath(root.right, targetSum - root.val, count)
    def dfs(self, root: Optional[TreeNode], targetSum: int,count: List[int]):
        if not root:
            return
        
        self.dfs(root.left, targetSum, count)
        self.countPath(root, targetSum, count)
        self.dfs(root.right, targetSum, count)
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = [0]
        self.dfs(root,targetSum,count)
        return count[0]
        