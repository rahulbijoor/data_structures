class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preq = []
            for p in prerequisites:
                if i == p[0]:
                    preq.append(p[1])
            preMap[i] = preq
        print(preMap)
        visited=set()
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            visited.add(course)
            for p in preMap[course]:
                if not dfs(p):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True