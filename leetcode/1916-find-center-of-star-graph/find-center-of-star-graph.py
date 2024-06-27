class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n1=edges[0][0]
        n2=edges[0][1]
        if n1 == edges[1][0] or n1 == edges[1][1]:
            return n1
        return n2