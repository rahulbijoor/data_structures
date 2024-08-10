class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n=len(rooms)
        visited = [False]*n
        visited[0] = True
        stack=[0]

        while stack:
            ele = stack.pop()
            for nei in rooms[ele]:
                if not visited[nei]:
                    visited[nei] = True
                    stack.append(nei)
        
        return all(visited)

            

        