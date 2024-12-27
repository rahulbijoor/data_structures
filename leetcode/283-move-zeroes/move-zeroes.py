class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = -1
        while i < len(nums):
            if nums[i]!= 0:
                if j+1 < len(nums):
                    nums[i],nums[j+1] = nums[j+1],nums[i]
                    j += 1
            i += 1        
        