class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        totalSum = ((n**2)*((n**2)+1))//2
        ht = set()
        res = []
        Sum = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                Sum += grid[r][c]
                if grid[r][c] not in ht:
                    ht.add(grid[r][c])
                else:
                    res.append(grid[r][c])
        missing = totalSum - (Sum-res[0]) 
        res.append(missing)
        return res
        
                    
