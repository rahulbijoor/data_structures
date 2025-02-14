class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False]*(l+1)
        dp[0] = True
        for i in range(1,l+1):
            for j in range(0,i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[l]
                    
