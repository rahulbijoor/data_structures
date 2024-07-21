# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper(node: TreeNode, maxVal: int) -> int:
            if not node:
                return 0
            rec=0
            if node.val >= maxVal:
                rec = 1
            maxVal = max(node.val, maxVal)
            return helper(node.left, maxVal) + helper(node.right, maxVal) + rec
        
        return helper(root,root.val)