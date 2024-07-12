class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        firstString = ""
        secondString =""
        if x>=y:
            firstString="ab"
            secondString="ba"
        else:
            secondString="ab"
            firstString="ba"
        result = 0
        stack=[]
        for char in s:
            if stack and char == firstString[1] and stack[-1] == firstString[0]:
                result += max(x,y)
                stack.pop()
            else:
                stack.append(char)
        
        newstack=[]
        for char in stack:
            if newstack and char == secondString[1] and newstack[-1] == secondString[0]:
                result += min(x,y)
                newstack.pop()
            else:
                newstack.append(char)
        return result
