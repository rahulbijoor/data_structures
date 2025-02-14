class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)
        dp = [False]*(l+1)
        dp[0] = True
        for i in range(1,l+1):
            for w in wordDict:
                l2 = len(w)
                if i >= l2 and dp[i-l2] and s[i-l2:i] in wordDict:
                    dp[i] = True
                    break
            
        return dp[l]
                    
