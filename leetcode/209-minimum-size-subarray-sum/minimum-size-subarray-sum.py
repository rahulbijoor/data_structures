class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        l = len(nums)
        res = float("inf")
        for right in range(l):
            total += nums[right]
            while total >= target:
                res = min(res,right-left+1)
                total -= nums[left]
                left += 1
        
        return 0 if res == float("inf") else res

                

