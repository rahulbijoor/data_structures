class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd = [1] * n
        rightProd = [1] * n
        for i in range(1,n):
            leftProd[i] = leftProd[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            rightProd[i] = rightProd[i+1]*nums[i+1]
        res = [1]*n
        for i in range(n):
            res[i] = leftProd[i] * rightProd[i] 
        return res
