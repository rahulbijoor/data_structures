# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None :
            return 0
        if (root.left is None and root.right is None ):
            return 1
        
        def helper(node: Optional[TreeNode]):
            if node is None: 
                return 0
            
            if (node.left is None  and node.right is None ):
                return 1
            
            if node.left is None:
                return 1+helper(node.right)
            if node.right is None:
                return 1+helper(node.left)

            return 1+min(helper(node.left),helper(node.right))
        
        return helper(root)
        