class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def helper(curr):
            if len(curr) == len(nums):
                res.append(copy.deepcopy(curr))
                return
            
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    helper(curr)
                    curr.pop()
                    
        helper([])
        return res