class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            Sum = nums[left] + nums[right]
            if Sum < k:
                left += 1
            elif Sum > k:
                right -= 1
            else:
                left += 1
                right -= 1
                count += 1
        return count

