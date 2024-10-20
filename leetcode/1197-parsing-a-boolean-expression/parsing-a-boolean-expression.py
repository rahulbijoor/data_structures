class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        s = expression
        i = 0
        
        def helper():
            nonlocal i
            c = s[i]
            i += 1

            if c == 't':
                return True
            if c == 'f':
                return False
            if c == '!':
                i += 1  # Skip '('
                res = not helper()
                i += 1  # Skip ')'
                return res
            
            children = []
            i += 1  # Skip '('
            while s[i] != ')':  # Loop until we find ')'
                if s[i] == ',':
                    i += 1  # Skip comma
                else:
                    children.append(helper())
            i += 1  # Skip ')'

            if c == '&':
                return all(children)
            if c == '|':
                return any(children)
        
        return helper()
