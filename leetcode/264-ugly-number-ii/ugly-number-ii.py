class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0]*n

        t2, t3, t5 = 0, 0, 0
        ugly[0] = 1
        for i in range(1, n):
            ugly[i] = min(ugly[t2]*2,min(ugly[t3]*3,ugly[t5]*5))
            if ugly[i] == ugly[t2]*2:
                t2 += 1
            if ugly[i] == ugly[t3]*3:
                t3 += 1
            if ugly[i] == ugly[t5]*5:
                t5 += 1
        
        return ugly[n-1]