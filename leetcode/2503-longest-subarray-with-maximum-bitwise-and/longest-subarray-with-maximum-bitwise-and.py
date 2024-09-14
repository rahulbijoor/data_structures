class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxAND = max(nums)
        result = 0
        maxLength = 0
        for i in range(len(nums)):
            
            if nums[i] == maxAND:
                maxLength += 1
            else:
                result = max(result,maxLength)
                maxLength = 0
        return max(result,maxLength)
