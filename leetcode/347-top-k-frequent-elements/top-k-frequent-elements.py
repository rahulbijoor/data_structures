class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for i in nums:
            if i in hm.keys():
                hm[i] += 1
            else:
                hm[i] = 1
        heap = []
        heapq.heapify(heap)
        for num in hm.keys():
            heapq.heappush(heap,(hm[num],num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res