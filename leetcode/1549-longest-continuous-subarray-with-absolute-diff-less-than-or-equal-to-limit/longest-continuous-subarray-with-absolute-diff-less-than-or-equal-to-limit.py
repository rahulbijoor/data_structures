class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        max_deque = deque()  # Deque to keep track of maximum values
        min_deque = deque()  # Deque to keep track of minimum values
        left = 0  # Left pointer of the sliding window
        max_length = 0  # Variable to store the maximum length of the valid subarray

        for right in range(len(nums)):
            # Update the max deque: remove elements from the back that are less than or equal to the current element
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # Update the min deque: remove elements from the back that are greater than or equal to the current element
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # Ensure the window is valid
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove elements from deques if they are out of the current window
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            # Update the maximum length of the valid subarray
            max_length = max(max_length, right - left + 1)

        return max_length

