class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if stack:
                    top = stack.pop()
                    if (top =='(' and ch == ')') or (top =='{' and ch == '}') or (top =='[' and ch ==']'):
                        continue
                    else:
                        return False
                else:
                    return False
        return not stack