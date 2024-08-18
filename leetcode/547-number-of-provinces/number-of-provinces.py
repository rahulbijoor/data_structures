class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited =[False]*len(isConnected)

        def dfs(n: int):
            visited[n] = True
            for i in range(0, len(isConnected)):
                if isConnected[n][i] == 1 and not visited[i]:
                    dfs(i)
            

        count = 0
        for i in range(0, len(isConnected)):
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count