class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp =[[-1]*n for i in range(m)]
        print(dp)
        def helper(i,j,dp):
            
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = helper(i+1, j, dp) + helper(i, j+1, dp)

            return dp[i][j]
        return helper(0, 0,dp)
        