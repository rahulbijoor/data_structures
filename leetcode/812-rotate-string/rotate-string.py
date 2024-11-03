class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        for i in range(len(s)):
            temp = s[1:]+s[0]
            if temp == goal:
                return True
            s = temp
        
        return False