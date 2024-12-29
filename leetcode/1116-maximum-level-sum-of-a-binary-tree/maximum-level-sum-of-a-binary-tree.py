class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        maxSum = root.val
        queue = deque([root])
        level = 0
        maxLevel = 1
        
        while queue:
            l = len(queue)
            level += 1
            levelSum = 0
            for _ in range(l):
                node = queue.popleft()
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Update maxSum and maxLevel only if levelSum is strictly greater
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level
        
        return maxLevel
        