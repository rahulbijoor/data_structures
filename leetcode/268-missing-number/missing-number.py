class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actualSum = 0
        currentSum = 0
        for i in range(len(nums)):
            actualSum += i+1
            currentSum += nums[i]
        return actualSum-currentSum