class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j = 0
        res = ""
        for i in range(len(s)):
            if j < len(spaces) and i == spaces[j]:
                res += ' ' 
                j += 1
            res += s[i]
                
        return res