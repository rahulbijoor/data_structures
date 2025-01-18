class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp =[-1]*(n+1)
        dp[0] = 1
        dp[1] = 1
        def helper(i):
            
            if dp[i] != -1:
                return dp[i]

            dp[i]=helper(i-1)+helper(i-2)
            return dp[i]
        helper(n)
        return dp[-1]
        