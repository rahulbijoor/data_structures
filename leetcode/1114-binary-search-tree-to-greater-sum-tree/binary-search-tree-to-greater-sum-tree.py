# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def ReverseInOrder(self, node: TreeNode):

            if node:
                ReverseInOrder(self, node.right)
                self.sum += node.val
                node.val = self.sum
                ReverseInOrder(self, node.left)
        ReverseInOrder(self, root)
        return root