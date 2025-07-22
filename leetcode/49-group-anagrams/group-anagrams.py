class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hm =  dict()
        for s in strs:
            c = Counter(s)
            t = tuple(sorted(c.items()))
            if t not in hm.keys():
                hm[t] = [s]
            else:
                hm[t].append(s)
        print(hm)
        return hm.values()
