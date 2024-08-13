# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=[]
        def Inorder(node,k):
            if not node:
                return
            
            Inorder(node.left,k-1)
            result.append(node.val)
            Inorder(node.right,k-1)
        
        Inorder(root,k)
        return result[k-1]
        