class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        votes = 1
        cand = nums[0]

        for i in range(1,len(nums)):
            if cand == nums[i]:
                votes += 1
            else:
                votes -= 1
            if votes == 0:
                cand = nums[i]
                votes = 1
        return cand
            