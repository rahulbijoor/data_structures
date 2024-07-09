class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows={}
        cols={}
        for i in range(0,len(grid)):
            st="/"
            for  j in range(0,len(grid)):
                
                st += ("/"+str(grid[i][j]))
                
            if st in rows.keys():
                rows[st] += 1
            else:
                rows[st] = 1
        for i in range(0,len(grid)):
            st="/"
            for  j in range(0,len(grid)):
                
                st += ("/"+str(grid[j][i]))
                
            if st in cols.keys():
                cols[st] += 1
            else:
                cols[st] = 1
        count = 0
        for key,value in rows.items():
            if key in cols.keys():
                count+=(rows[key]*cols[key])
        return count