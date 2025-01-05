class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = sum(shifts)
        res =""
        for i in range(len(shifts)):
            f = ((ord(s[i])-ord('a')) + total)%26 
            f = f+ord('a')
            ch = chr(f)
            res += ch
            total -= shifts[i]
        return res