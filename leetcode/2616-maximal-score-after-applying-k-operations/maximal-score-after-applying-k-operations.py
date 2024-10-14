import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        for i in range(len(nums)):
            nums[i] = -1 * nums[i]
        

        heapq.heapify(nums)

        while k > 0:
            maxEle = -1 * heapq.heappop(nums)
            score += maxEle
            maxEle = (maxEle+2)//3
            heapq.heappush(nums,-1*maxEle)
            k -= 1

        return score
