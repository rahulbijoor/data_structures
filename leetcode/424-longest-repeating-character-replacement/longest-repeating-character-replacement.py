class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        freq = {}
        windowlen =0
        res  = 0
        for r in range(len(s)):
            if s[r] not in freq.keys():
                freq[s[r]]=1
            else:
                freq[s[r]] += 1

            max_freq = max(freq.values())

            while (r - l + 1) - max_freq > k:
                freq[s[l]] -= 1
                l += 1 
            res = max(res,(r-l+1))
        return res    
        
