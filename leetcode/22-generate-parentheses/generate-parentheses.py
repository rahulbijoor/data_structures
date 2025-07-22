class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def helper(open_b,close,st,res):
            if open_b == close == n:
                res.append(st)
                return
            if open_b > n:
                return
            if close > open_b:
                return
            
            helper(open_b+1,close,st+"(",res)
            helper(open_b,close+1,st+")",res)
        helper(0,0,"",res)
        return res