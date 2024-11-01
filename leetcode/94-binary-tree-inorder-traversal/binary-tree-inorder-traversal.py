# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        result = []
        def InOrder(node: Optional[TreeNode],res : List[int]):
            if node is None:
                return
            
            InOrder(node.left,res)
            res.append(node.val)
            InOrder(node.right,res)
        
        InOrder(root,result)
        return result