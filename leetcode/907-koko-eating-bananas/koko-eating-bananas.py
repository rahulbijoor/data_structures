class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        Max=max(piles)
        low=1
        high=Max
        while low < high:
            mid = (low+high)//2
            hours = 0
            for p in piles:
                hours+= ceil(p / mid)
            if hours <= h:
                high=mid
            else:
                low=mid+1
        return low