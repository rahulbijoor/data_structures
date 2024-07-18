# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], targetSum: int, sum: int) -> bool:
        if not node:
            
            return False
        sum+=node.val
        if not node.left and not node.right:
            if targetSum == sum:
                return True
                
         
        return self.dfs(node.left, targetSum, sum) or self.dfs(node.right, targetSum, sum)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root, targetSum, 0)     