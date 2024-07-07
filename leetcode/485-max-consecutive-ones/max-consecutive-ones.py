class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        maxOnes=0
        Ones=0
        while left < len(nums):
            if nums[left] == 1:
                Ones += 1
                if maxOnes < Ones:
                    maxOnes = Ones
            else:
                
                Ones = 0
            left += 1
        return maxOnes