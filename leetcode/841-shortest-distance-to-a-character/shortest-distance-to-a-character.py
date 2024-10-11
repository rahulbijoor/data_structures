class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def helper(i: int,dist: int) -> None:

            if i < 0 or i >= len(s) or pos[i] <= dist:
                return
            
            pos[i] = dist
            helper(i+1,dist+1)
            helper(i-1,dist+1)

        pos = [len(s) for i in range(len(s))]
        for i,ch in enumerate(s):
            if ch == c:
                helper(i,0)

        
        
        return pos