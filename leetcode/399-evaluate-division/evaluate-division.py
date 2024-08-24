from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        indexes = {}
        count = 0
        for x, y in equations:
            if x not in indexes:
                indexes[x] = count
                count += 1
            if y not in indexes:
                indexes[y] = count
                count += 1
                
        graph = [[0] * len(indexes) for _ in range(len(indexes))]
        
        for i in range(len(equations)):
            graph[indexes[equations[i][0]]][indexes[equations[i][1]]] = values[i]
            graph[indexes[equations[i][1]]][indexes[equations[i][0]]] = 1 / values[i]
        
        def dfs(source, destination, visited, distance):
            if source == destination:
                return distance
            
            visited[source] = True
            
            for neighbor in range(len(graph)):
                if graph[source][neighbor] != 0 and not visited[neighbor]:
                    result = dfs(neighbor, destination, visited, distance * graph[source][neighbor])
                    if result != -1:  # If a valid path is found
                        return result
            
            return -1
        
        def helper(query):
            if query[0] not in indexes or query[1] not in indexes:
                return -1
            if query[0] == query[1]:
                return 1
            visited = [False] * len(graph)
            return dfs(indexes[query[0]], indexes[query[1]], visited, 1)
        
        result = []
        for query in queries:
            result.append(helper(query))
        return result


