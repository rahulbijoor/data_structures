class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1,1])
        if numRows == 2:
            
            return res
        currRows = 3
        print(res)
        while currRows <= numRows:
            curr=[1]*currRows
            for i in range(1,currRows-1):
                curr[i] = res[currRows-2][i-1] + res[currRows-2][i]
            res.append(curr)
            currRows += 1
        return res
