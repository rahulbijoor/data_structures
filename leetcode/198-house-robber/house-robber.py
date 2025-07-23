class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        dp = [-1]*(len(nums)+1)
        dp[0] = nums[0]
        
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1],nums[0])
        dp[1] = max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(nums[i] + dp[i-2],dp[i-1])
        
        return dp[n-1]
