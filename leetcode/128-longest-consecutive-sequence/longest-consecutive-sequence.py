class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        max_seq = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr_num = num
                curr_seq = 1

                while curr_num + 1 in nums_set:
                    curr_seq += 1
                    curr_num += 1

                max_seq = max(curr_seq, max_seq)

        return max_seq