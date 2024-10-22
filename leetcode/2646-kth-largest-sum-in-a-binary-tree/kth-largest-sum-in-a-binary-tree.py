import heapq
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        if not root:
            return -1
        
        min_heap = []
        queue = deque([root])
        level_count = 0  # To keep track of how many levels we have
        
        while queue:
            level_size = len(queue)
            level_sum = 0
            
            for _ in range(level_size):
                curr = queue.popleft()
                level_sum += curr.val
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            level_count += 1
            heapq.heappush(min_heap, level_sum)
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # If there are fewer levels than k, return -1
        if level_count < k:
            return -1
        
        # The root of the heap now contains the k-th largest level sum
        return min_heap[0] if min_heap else -1
