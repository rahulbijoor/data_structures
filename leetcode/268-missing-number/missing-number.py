class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        TotalSum = 0
        ActualSum = 0
        n = len(nums)
        for i in range(n):
            TotalSum += (i+1)
            ActualSum += nums[i]

        return TotalSum - ActualSum