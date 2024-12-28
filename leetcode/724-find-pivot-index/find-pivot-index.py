class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        l = len(nums)
        leftSum =[0]*l
        rightSum = [0]*l
        for i in range(1,l):
            leftSum[i] = leftSum[i-1] + nums[i-1]
        for i in range(l-2,-1,-1):
            rightSum[i] = rightSum[i+1] + nums[i+1]
            
        for i in range(l):
            if leftSum[i] == rightSum[i]:
                return i 
        
        return -1