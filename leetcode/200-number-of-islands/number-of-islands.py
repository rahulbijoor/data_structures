class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        print(visited)
        def bfs(row: int,col: int):
            q = collections.deque()
            q.append((row,col))
            visited[row][col] = True

            while q:
                row, col = q.popleft()
                moves=[(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
                for new_row, new_col in moves:
                    if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]) and grid[new_row][new_col] == "1" and not visited[new_row][new_col]:
                        visited[new_row][new_col] = True
                        q.append((new_row,new_col))
                    
        count = 0
        for row in range(len(grid)):

            for col in range(len(grid[0])):

                if not visited[row][col] and grid[row][col] == "1":
                    bfs(row,col)
                    count += 1
        print(visited)
        return count