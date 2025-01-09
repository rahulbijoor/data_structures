class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        l1 = len(pref)
        count = 0
        for w in words: 
            if l1 <= len(w) and pref == w[:l1]:
                count += 1
        return count