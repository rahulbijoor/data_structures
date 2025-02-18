class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = nums[0]
        lastnum = nums[0]
        for i in range(1,len(nums)):
            if lastnum < nums[i]:
                curSum += nums[i]
            else:
                maxSum = max(maxSum, curSum)
                curSum = nums[i]
            
            lastnum = nums[i]

        return max(maxSum, curSum)

            
        return maxSum
