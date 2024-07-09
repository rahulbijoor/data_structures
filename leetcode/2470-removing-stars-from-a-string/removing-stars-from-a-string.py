class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        top=-1
        for i in range(0,len(s)):
            if s[i] != "*":
                stack.append(s[i])
                top += 1
            else:
                if top >= 0:
                    stack.pop(top)
                    top -= 1
        res = ""
        for i in range(0,len(stack)):
            res+=stack[i]
        return res

