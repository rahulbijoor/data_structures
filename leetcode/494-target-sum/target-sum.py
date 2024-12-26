class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)
        i = 0
        memo = {}
        def helper(nums,target,i):
            if i == len(nums) and target == 0:
                return 1
            if i == len(nums): 
                return 0
            if (i, target) in memo:
                return memo[(i,target)]
            
            add = helper(nums,target-nums[i],i+1)
            sub = helper(nums,target+nums[i],i+1)
            memo[(i, target)] = add + sub
            return memo[(i, target)]

        return helper(nums,target,0)