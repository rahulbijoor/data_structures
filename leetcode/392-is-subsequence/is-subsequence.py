class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1=0
        l2=0
        while l1<len(s) and l2<len(t):
            if s[l1] == t[l2]:
                l1 += 1
            l2 += 1
        print(l1,l2)
        return l1 == len(s)        