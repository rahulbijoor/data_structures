class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxSoFar = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            maxSoFar = max(prices[i],maxSoFar)
            maxProfit= max(maxProfit,maxSoFar-prices[i])

        return maxProfit