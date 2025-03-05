class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = 1
        if n <= 1:
            return n
        for i in range(2,n+1):
            dp += (4*(i-1))
        
        return dp
        