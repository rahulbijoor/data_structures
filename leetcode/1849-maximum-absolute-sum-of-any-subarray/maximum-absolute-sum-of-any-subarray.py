class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        l = 0
        r = 0
        maxSum = float("-inf")
        minSum = float("inf")
        curPosSum = 0
        curNegSum = 0
        for n in nums:
            curPosSum = max(n,curPosSum+n)
            curNegSum = min(n,curNegSum+n)
            maxSum = max(curPosSum,maxSum)
            minSum = min(curNegSum,minSum)
            
        return max(abs(maxSum),abs(minSum)) 
                 