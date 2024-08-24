class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = [[False]*len(maze[0]) for _ in range(len(maze))]
        q = collections.deque()
        q.append((entrance[0], entrance[1], 0))
        visited[entrance[0]][entrance[1]] = True
         
        while q:
            row , col, count = q.popleft()
            moves = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]
            for move in moves:
                new_row = move[0]
                new_col = move[1]
                if new_row >= 0 and new_col >= 0 and new_row < len(maze) and new_col < len(maze[0]) and maze[new_row][new_col] == "." and not visited[new_row][new_col]:
                    if new_row == 0 or new_col == 0 or new_row == len(maze)-1 or new_col == len(maze[0])-1:
                        return count+1
                    else:
                        visited[new_row][new_col] = True
                        q.append((new_row, new_col,count+1))
            
        
        return -1
        
                

