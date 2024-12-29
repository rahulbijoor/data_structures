# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        list1 = []
        list2 = []
        def helper(node,list):
            if not node:
                return
            if not node.left and not node.right:
                list.append(node.val)
                return
            
            helper(node.left,list)
            helper(node.right,list)

        helper(root1,list1)
        helper(root2,list2)
        if len(list1) != len(list2):
            return False
        
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True
        