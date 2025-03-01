class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        i = -1
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i+1],nums[j] = nums[j],nums[i+1]
                i += 1
            j+=1

        return nums