# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque()
        q.append(root)
        res = []
        while q:
            curr = q.popleft()
            if curr:
                res.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                res.append("#")
        print(res)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        values = data.split(",")
        if values[0] == "#":
            return None
        root = TreeNode(values[0])
        q = deque()

        q.append(root)
        i = 1
        while q and i < len(values):
            curr = q.popleft()
            if values[i] != "#":
                left = TreeNode(values[i])
                curr.left = left
                q.append(left)
            i += 1
            if values[i] != "#":
                right = TreeNode(values[i])
                curr.right = right
                q.append(right)
            i += 1
        return root

        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))