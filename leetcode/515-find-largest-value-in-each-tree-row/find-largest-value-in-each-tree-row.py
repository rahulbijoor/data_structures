# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        maxVal = []
        if not root:
            return maxVal
        queue = deque()
        queue.append(root)
        while queue:
            
            l = len(queue)
            mVal = float('-inf')
            for _ in range(l):
                ele = queue.popleft()
                mVal = max(mVal, ele.val) 
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                print(ele.val)
            maxVal.append(mVal)
        return maxVal


        