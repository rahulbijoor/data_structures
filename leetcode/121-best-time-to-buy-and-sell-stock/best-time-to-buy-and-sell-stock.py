class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxSoFar = 0
        for i in range(len(prices)-1,-1,-1):
            maxSoFar = max(prices[i],maxSoFar)
            maxProfit= max(maxProfit,maxSoFar-prices[i])

        return maxProfit