class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        h = len(nums)-1
        mid =0
        while l < h:
            mid = l + (h-l)//2
            if nums[mid] > nums[h]:
                l = mid+1
            else:
                h = mid
        return nums[l]
        