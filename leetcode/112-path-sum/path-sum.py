# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def helper(node: Optional[TreeNode], targetSum: int) -> bool:
            if not node:
                return False
            
            targetSum-= node.val
            if targetSum == 0 and not node.left and not node.right:
                return True
            
            return helper(node.left, targetSum) or helper(node.right,targetSum)
        

        return helper(root, targetSum)