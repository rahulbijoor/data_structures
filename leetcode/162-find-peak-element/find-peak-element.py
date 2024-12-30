class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = float('-inf')
        for i in range(len(nums)):
            next  = 0
            if i+1 < len(nums):
                next = nums[i+1]
            else:
                next = float('-inf')
            if prev < nums[i] > next:
                return i

        