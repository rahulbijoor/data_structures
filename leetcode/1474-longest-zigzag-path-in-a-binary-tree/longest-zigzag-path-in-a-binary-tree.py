# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        def helper(node,currCount,isLeft):
            if not node:
                return currCount - 1
            if isLeft:
                leftPath  = helper(node.left,1,True)
                rightPath  = helper(node.right,currCount+1,False)
            else:
                leftPath  = helper(node.left,currCount+1,True)
                rightPath  = helper(node.right,1,False)


            return max(leftPath,rightPath)
        leftPath = helper(root.left,1,True)
        rightPath = helper(root.right,1,False) 
        return max(leftPath,rightPath)
        