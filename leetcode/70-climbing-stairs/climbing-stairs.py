class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        mp=[-1]*(n+1)
        mp[0] = 0
        mp[1] = 1
        mp[2] = 2
        def helper(n,mp):
            if mp[n] != -1:
                return mp[n]
            mp[n] = helper(n-1,mp) + helper(n-2,mp)
            return mp[n]
        
        helper(n,mp)
        return mp[n]