class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh_oranges = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        if fresh_oranges == 0:
            return 0
        count = 0
        while q:
            count+= 1
            for _ in range(len(q)):

                row, col = q.popleft()
            
                moves = [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]
                for move in moves:
                    new_row = move[0]
                    new_col = move[1]
                    if new_row >= 0 and new_col >= 0 and new_row < len(grid) and new_col < len(grid[0]) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        q.append((new_row,new_col))
                        fresh_oranges -= 1
           
                
        if fresh_oranges == 0:
            return count-1
        return -1
                


        

