from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Create a set of directed edges and a dictionary for neighbor lists
        edges = set()
        neighbours = {i: [] for i in range(n)}
        
        for a, b in connections:
            edges.add((a, b))  # Directed edge from a to b
            neighbours[a].append(b)
            neighbours[b].append(a)
        
        visit = set()
        changes = 0
        
        def dfs(city):
            nonlocal changes
            
            for neighbour in neighbours[city]:
                if neighbour in visit:
                    continue
                # Check if this edge needs to be reversed
                if (city, neighbour) in edges:
                    changes += 1
                visit.add(neighbour)
                dfs(neighbour)
        
        # Start DFS from city 0
        visit.add(0)
        dfs(0)
        
        return changes
