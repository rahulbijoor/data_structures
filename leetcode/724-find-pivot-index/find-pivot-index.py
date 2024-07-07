class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalSum = 0
        leftSum = 0
        for num in nums:
            totalSum += num
        for i in range(0,len(nums)):
            if leftSum == totalSum - ( leftSum + nums[i]):
                return i
            leftSum += nums[i]
        return -1


        