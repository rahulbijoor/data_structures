class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
    
    # Step 2: Sort the array using the custom key
    # Key is (frequency, -value) to sort by frequency first and then by value in decreasing order
        sorted_nums = sorted(nums, key=lambda x: (counter[x], -x))
    
        return sorted_nums
