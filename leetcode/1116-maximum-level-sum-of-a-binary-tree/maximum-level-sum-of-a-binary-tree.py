# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = [root]
        level = 1
        maxLevel = 1
        maxSum = root.val
        
        while queue:
            level_length = len(queue)
            current_sum = 0
            
            for _ in range(level_length):
                node = queue.pop(0)
                current_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if current_sum > maxSum:
                maxSum = current_sum
                maxLevel = level
            
            level += 1
        
        return maxLevel