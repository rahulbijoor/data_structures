class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        totalSum = ((n**2)*((n**2)+1))//2
        ht = {}
        res = []
        Sum = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                Sum += grid[r][c]
                if grid[r][c] not in ht.keys():
                    ht[grid[r][c]] = 1
                else:
                    res.append(grid[r][c])
        missing = totalSum - (Sum-res[0]) 
        res.append(missing)
        return res
        
                    
