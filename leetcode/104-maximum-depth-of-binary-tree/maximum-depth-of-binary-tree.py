# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def helper(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            
            leftDepth = helper(node.left)
            rightDepth = helper(node.right)

            return 1+ max(leftDepth,rightDepth)
        
        return helper(root)