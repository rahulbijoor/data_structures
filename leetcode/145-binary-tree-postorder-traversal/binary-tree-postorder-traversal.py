# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postOrder(self, node, result):
        if not node:
            return
        
        self.postOrder(node.left, result)
        self.postOrder(node.right, result)
        result.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        self.postOrder(root,result)
        return result
        