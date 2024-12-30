class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def comb(curr, k, n, start):
            if k == 0 and n == 0:
                res.append(curr)
                return
            if k <= 0:
                return
            for i in range(start, min(10, n+1)):
                comb(curr+[i],k-1,n-i,i+1)
        comb([], k, n, 1)
        return res

        

        