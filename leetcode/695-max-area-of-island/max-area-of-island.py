class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        if not grid and grid[0]:
            return 0
        def dfs(row: int, col: int) -> int:
            if row < 0 or row >= len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return (dfs(row + 1, col)+dfs(row - 1, col)+dfs(row, col-1)+dfs(row, col + 1))+1


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row,col))

        return maxArea
        

        