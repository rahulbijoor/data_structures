class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        res = []
        l = len(code)
        for i in range(l):
            if k == 0:
                res.append(0)
            elif k > 0:
                res.append(sum(code[(i+j)%l] for j in range(1,k+1)))
            else:
                res.append(sum(code[(i+j)%l] for j in range(k,0)))
        
        return res