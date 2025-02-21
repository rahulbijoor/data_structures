class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = -sys.maxsize - 1
        Sum = 0
        for n in nums:
            Sum += n
            maxSum = max(maxSum,Sum)
            if Sum  < 0:
                Sum = 0
            
        return maxSum


