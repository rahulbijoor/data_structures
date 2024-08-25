class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = len(nums)
        pq = []
        heapq.heapify(pq)
        count = l-k
        for n in nums:
            heapq.heappush(pq,n)
        while count != 0:
            heapq.heappop(pq)
            count -= 1
        return heapq.heappop(pq)