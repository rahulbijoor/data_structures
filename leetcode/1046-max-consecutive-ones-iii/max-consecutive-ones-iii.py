class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
         """
        count = 0
        left = 0
        maxOnes=0
        right=0
        while right < len(nums):
            if nums[right] == 0:
                count += 1
            while count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
                

            if maxOnes < right-left+1:
                maxOnes = right-left+1
            right += 1

        return maxOnes