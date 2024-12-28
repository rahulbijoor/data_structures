class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        l1 = len(s)
        l2 = len(t)

        if l1 > l2:
            return False
        
        while j < l2:
            if i == l1:
                return True

            if s[i] == t[j]:
                i += 1
            j += 1
        if i == l1:
            return True

        
        return False


        