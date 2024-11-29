class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        maxEle = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            maxPro = max(maxPro, maxEle - prices[i])
            maxEle = max(maxEle,prices[i])
            
        return maxPro
