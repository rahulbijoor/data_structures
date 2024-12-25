# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        def minSwapsToSort(arr):
            n = len(arr)

            # Pair values with their indices
            indexed_arr = [(value, index) for index, value in enumerate(arr)]
            # Sort the array by value
            indexed_arr.sort(key=lambda x: x[0])
    
            visited = [False] * n  # Track visited elements
            swaps = 0
    
            for i in range(n):
                if visited[i] or indexed_arr[i][1] == i:
                    continue

                # Calculate the size of the cycle
                cycle_size = 0
                x = i
        
                while not visited[x]:
                    visited[x] = True
                    next_index = indexed_arr[x][1]
                    x = next_index
                    cycle_size += 1

                if cycle_size > 1:
                    swaps += (cycle_size - 1)
    
            return swaps

        minSwap = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            level = []
            l = len(queue)
            
            for _ in range(l):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Calculate minimum swaps for the current level
            minSwap += minSwapsToSort(level)
        
        return minSwap