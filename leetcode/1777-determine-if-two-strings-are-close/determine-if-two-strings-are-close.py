class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        fq1 = {}
        fq2 = {}
        for w in word1:
            if w in fq1.keys():
                fq1[w] += 1
            else:
                fq1[w] = 1
        
        for w in word2:
            if w in fq2.keys():
                fq2[w] += 1
            else:
                fq2[w] = 1

        return set(fq1.keys()) == set(fq2.keys()) and sorted(fq1.values())== sorted(fq2.values())