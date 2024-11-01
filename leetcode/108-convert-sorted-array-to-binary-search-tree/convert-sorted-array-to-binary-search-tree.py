# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        

        def helper(nums: List[int], start, end):
            if start > end:
                return
            
            mid = start + (end-start)//2
            node = TreeNode(nums[mid])
            node.left = helper(nums,start,mid-1)
            node.right = helper(nums,mid+1,end)
            return node
        
        return helper(nums,0,len(nums)-1)