class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        leftProd =[1]*len(nums)
        for i in range(1,l):
            leftProd[i] = leftProd[i-1]*nums[i-1]
        rightProd = 1
        for j in range(l-2,-1,-1):
            rightProd = rightProd*nums[j+1]
            leftProd [j] *= rightProd 
        return leftProd
        
        