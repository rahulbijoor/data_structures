class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        list=[0]*(n+1)
        list[1] = 1
        list[2] = 1
        for i in range(3,n+1):
            list[i]=list[i-1]+list[i-2]+list[i-3]
        
        return list[n]