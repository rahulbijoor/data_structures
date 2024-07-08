class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ht={}
        for a in arr:
            if a in ht.keys():
                ht[a] += 1
            else:
                ht[a] = 1

        return len(ht.values()) == len(set(ht.values()))  