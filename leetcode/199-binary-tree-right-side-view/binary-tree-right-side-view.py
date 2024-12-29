# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            l = len(queue)
            row = []
            for i in range(l):
                ele = queue.popleft()
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                row.append(ele.val)
            res.append(row[-1])
        return res