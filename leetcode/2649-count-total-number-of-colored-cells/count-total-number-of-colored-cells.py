class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(5)
        if n <= 2:
            return dp[n]
        curr = 4
        for i in range(3,n+1):
            dp.append(dp[i-1]+curr+4)
            curr += 4
        
        return dp[-1]
        