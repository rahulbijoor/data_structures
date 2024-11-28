class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {} 
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in ht:  
                return [ht[complement], i]  
            ht[nums[i]] = i  
