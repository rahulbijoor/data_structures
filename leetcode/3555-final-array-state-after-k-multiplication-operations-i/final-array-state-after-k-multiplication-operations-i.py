class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        indexed_nums = [(value, idx) for idx, value in enumerate(nums)]
        heapq.heapify(indexed_nums)
    
   
        for _ in range(k):
            smallest, idx = heapq.heappop(indexed_nums)
            heapq.heappush(indexed_nums, (smallest * multiplier,idx))
        result = [0]*len(nums)
        for value, idx in indexed_nums:
            result[idx] = value
        return result
        