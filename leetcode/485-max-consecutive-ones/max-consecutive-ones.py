class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_ones = 0
        max_ones = 0
        for n in nums:
            if n == 1:
                curr_ones = curr_ones + 1
                max_ones = max(curr_ones, max_ones)
            else:
                curr_ones = 0
        return max_ones
