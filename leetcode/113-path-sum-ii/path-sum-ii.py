# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], targetSum: int, sum: int,paths: List[List],path: List[int]):
        if not node:
            return
        sum+=node.val
        path.append(node.val)
        if not node.left and not node.right:
            if targetSum == sum:
                paths.append(list(path)) 
        else: 
            self.dfs(node.left, targetSum, sum, paths, path)
            self.dfs(node.right, targetSum, sum, paths, path)
        path.pop()
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths=[]
        path=[]
        self.dfs(root, targetSum, 0, paths, path)
        return paths
        