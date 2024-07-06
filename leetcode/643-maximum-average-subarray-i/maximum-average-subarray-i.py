class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        maxSum = 0
        for j in range(0,k):
            maxSum += nums[j]
        i += 1
        Sum = maxSum
        while i <= len(nums) - k :
            Sum = Sum - nums[i-1] + nums[k+i-1]
            if maxSum < Sum:
                maxSum = Sum
            i += 1
        return maxSum/k
