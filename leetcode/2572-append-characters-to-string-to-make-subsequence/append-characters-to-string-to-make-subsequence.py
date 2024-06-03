class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        strack=0
        ttrack=0
        while strack < len(s) and ttrack < len(t) :
            if s[strack] == t[ttrack]:
                ttrack += 1
            strack += 1
        
        return len(t)-ttrack