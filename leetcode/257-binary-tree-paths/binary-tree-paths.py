# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        def helper(node: Optional[TreeNode],currPath: List[str],allPath: List[str]) -> None:
            if not node:
                return
            
            currPath.append(str(node.val))

            if not node.right and not node.left:
                allPath.append("->".join(currPath))
            
            helper(node.left, currPath, allPath)
            helper(node.right, currPath, allPath)

            currPath.pop()
        
        currPath=[]
        allPath=[]
        helper(root, currPath, allPath)
        return allPath

