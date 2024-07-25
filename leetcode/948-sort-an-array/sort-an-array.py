class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(nums: List[int], low: int, high: int):
            if low < high:
                mid = low + (high - low) // 2
                mergeSort(nums, low, mid)
                mergeSort(nums, mid + 1, high)
                merge(nums, low, mid, high)

        def merge(nums: List[int], low: int, mid: int, high: int):
            leftSubArray = nums[low:mid + 1]
            rightSubArray = nums[mid + 1:high + 1]

            i = 0
            j = 0
            k = low

            while i < len(leftSubArray) and j < len(rightSubArray):
                if leftSubArray[i] <= rightSubArray[j]:
                    nums[k] = leftSubArray[i]
                    i += 1
                else:
                    nums[k] = rightSubArray[j]
                    j += 1
                k += 1

            while i < len(leftSubArray):
                nums[k] = leftSubArray[i]
                i += 1
                k += 1

            while j < len(rightSubArray):
                nums[k] = rightSubArray[j]
                j += 1
                k += 1
        
        mergeSort(nums, 0, len(nums) - 1)
        return nums