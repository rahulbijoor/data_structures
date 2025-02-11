class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1]*(n+1)
        dp[0] = 1
        dp[1] = 1
        def helper(n,dp):
            if dp[n] != -1:
                return dp[n]
            dp[n] = helper(n-1,dp)+helper(n-2,dp)
            return dp[n]
        helper(n,dp)
        return dp[n]