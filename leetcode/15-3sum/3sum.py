
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        res = []
        
        for i in range(len(nums) - 2):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer technique
            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                
                if current_sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for the second and third numbers
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move pointers
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1  # Increase sum
                else:
                    right -= 1  # Decrease sum
        
        return res
