from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        res = [0] * n
        start, end = (1, k) if k > 0 else (k, -1)
        window_sum = sum(code[i % n] for i in range(start, end + 1))
        
        for i in range(n):
            res[i] = window_sum

            window_sum -= code[(i + start) % n]
            window_sum += code[(i + end + 1) % n]
        
        return res
