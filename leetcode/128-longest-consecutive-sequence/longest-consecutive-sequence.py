class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = set(nums)
    
        # Step 2: Initialize the variable to track the longest sequence length
        max_length = 0
    
        # Step 3: Loop through each number in the set
        for num in st:
            # Check if it's the start of a sequence
            if num - 1 not in st:
                current_num = num
                current_length = 1
            
            # Count the length of the sequence
                while current_num + 1 in st:
                    current_num += 1
                    current_length += 1
            
            # Update the maximum length
                max_length = max(max_length, current_length)
    
        return max_length
