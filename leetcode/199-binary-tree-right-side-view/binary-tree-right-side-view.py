# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
            result=[]
            if not root:
                return result
            
            queue=[]
            queue.append(root)
            while queue:
                level_length = len(queue)
                for i in range(level_length):
                    node=queue.pop(0)
                    if i == level_length - 1:
                        result.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            return result
                