class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        h=[]
        heapq.heapify(nums)
        min1 = heapq.heappop(nums)
        min2 = heapq.heappop(nums)
        count = 0
        while min1 < k:
            nele = min(min1,min2)*2 + max(min1,min2)
            count += 1
            heapq.heappush(nums, nele)
            if len(nums) <=1:
                return count
            min1 = heapq.heappop(nums)
            min2 = heapq.heappop(nums)
        return count
