class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = 1
        while low < high:
            mid = low + (high-low)//2
            hours = 0
            for i in range(len(piles)):
                hours += ceil(piles[i]/mid)
            if hours > h:
                low = mid+1
            else:
                high = mid
        return low

