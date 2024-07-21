# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        def dfs(node: Optional[TreeNode], targetSum: int) -> int:
            if not node:
                return 0

            paths=helper(node, targetSum)
            leftpath=dfs(node.left, targetSum) 
            rightpath=dfs(node.right, targetSum)
            return leftpath + rightpath + paths
        
        def helper(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0
            rec=0
            if (target - node.val) == 0:
                rec=1
            return helper(node.left, target-node.val) + helper(node.right, target-node.val) + rec
        return dfs(root,targetSum)