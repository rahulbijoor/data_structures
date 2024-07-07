class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        count = 0
        maxOnes=0
        while right < len(nums):
            if nums[right]== 0:
                count += 1
            if count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            if maxOnes < right - left :
                maxOnes = right - left 
            right += 1
        return maxOnes