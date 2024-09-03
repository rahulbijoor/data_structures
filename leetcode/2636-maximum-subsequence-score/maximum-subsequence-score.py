class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        result = 0
        prefixSum = 0
        hp = []
        heapq.heapify(hp)
        for a,b in sorted(list(zip(nums1, nums2)), key = itemgetter(1), reverse = True):
            prefixSum += a
            heapq.heappush(hp,a)
            if len(hp) == k:
                result = max(result, prefixSum*b)
                prefixSum -= heapq.heappop(hp)
        return result