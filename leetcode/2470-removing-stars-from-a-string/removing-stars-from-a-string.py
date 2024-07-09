class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(0,len(s)):
            if s[i] != "*":
                stack.append(s[i])
            else:
                stack.pop()
        res = ""
        for i in range(0,len(stack)):
            res+=stack[i]
        return res

