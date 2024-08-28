class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        l = 1
        h = n-2
        while l <= h:
            m = l+(h-l)//2
            nums_length = len(nums)
            if  nums[(m - 1) % nums_length] < nums[m % nums_length] > nums[(m + 1) % nums_length]:
                return m
            elif nums[(m + 1) % nums_length] > nums[m % nums_length]:
                l = (m+1)
            elif nums[(m - 1) % nums_length] > nums[m % nums_length]:
                h = (m-1)
            
        
