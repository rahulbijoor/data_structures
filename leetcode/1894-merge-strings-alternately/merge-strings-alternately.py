class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1 = len(word1)
        l2 = len(word2) 
        i,j = 0,0
        res = ""
        while i < l1 and j < l2:
            res += (word1[i]+word2[j])
            i += 1
            j += 1
        print(word2[j:])
        if i < l1:
            res += (word1[i:])
        
        if j < l2:
            res += (word2[j:])
        return res