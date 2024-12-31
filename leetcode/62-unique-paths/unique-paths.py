class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp =[[-1]*n for i in range(m)]
        print(dp)
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        print(dp)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] =dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
        """def helper(i,j,dp):
            
            if i == m-1 and j == n-1:
                return 1
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = helper(i+1, j, dp) + helper(i, j+1, dp)

            return dp[i][j]
        return helper(0, 0,dp)
        """