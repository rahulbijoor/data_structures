class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preq =[]
            for p in prerequisites:
                if p[0] == i:
                    preq.append(p[1])
            preMap[i] = preq
        visited=set()
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            visited.add(course)
            for nei in preMap[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
