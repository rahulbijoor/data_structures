# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: Optional[TreeNode], k: List[int]) -> int:
        if not node:
            return None
        
        left = self.helper(node.left,k)
        if left:
            return left
        k[0] -= 1
        if k[0] == 0:
            return node.val
        right = self.helper(node.right,k)
        if right:
            return right
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result=0
        def helper(node: Optional[TreeNode]):
            nonlocal k
            nonlocal result

            if not node or k < 0:
                return

            helper(node.left)
            k -= 1
            if k == 0:
                result = node.val
                return
            helper(node.right)
        helper(root)
        return result
        