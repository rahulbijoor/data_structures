# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxDepth = 0
        def height(node):
            if not node:
                return 0
            
            return max(height(node.left),height(node.right)) + 1
        maxDepth = height(root)
        return maxDepth
        
            

        