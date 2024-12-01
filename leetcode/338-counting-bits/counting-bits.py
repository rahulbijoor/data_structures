class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        i = 0
        while i <= n:
            res.append(bin(i).count("1"))
        
            i += 1
        return res