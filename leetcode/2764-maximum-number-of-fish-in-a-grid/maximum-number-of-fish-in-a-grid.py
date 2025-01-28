class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        maxFish = 0
        def dfs(row,col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:

                return 0

            curFish = grid[row][col]
            grid[row][col] = 0
            curFish += dfs(row+1, col)
            curFish += dfs(row-1, col)
            curFish += dfs(row, col+1)
            curFish += dfs(row, col-1) 
            return curFish
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                
                maxFish = max(dfs(r,c),maxFish)
        return maxFish