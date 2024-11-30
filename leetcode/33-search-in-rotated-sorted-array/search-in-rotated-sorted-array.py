
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # Check if mid is the target
            if nums[mid] == target:
                return mid

            # Determine which half is sorted
            if nums[low] <= nums[mid]:  # Left half is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Target is in the sorted left half
                else:
                    low = mid + 1  # Target is in the right half
            else:  # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1  # Target is in the sorted right half
                else:
                    high = mid - 1  # Target is in the left half

        return -1  # Target not found
