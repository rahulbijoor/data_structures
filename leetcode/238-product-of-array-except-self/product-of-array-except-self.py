class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProd = 1
        leftProd =[1]*len(nums)

        for i in range(1,len(nums)):
            leftProd[i] = leftProd[i-1]*nums[i-1]
        
        for j in range(len(nums)-2,-1,-1):
            rightProd  = rightProd *nums[j+1]
            leftProd[j] =leftProd[j]*rightProd
        return leftProd

        