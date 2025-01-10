class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        
        max_count = Counter()
        for w in words2:
            word_count = Counter(w)
            for c in word_count:
                max_count[c] = max(max_count[c],word_count[c])
        res =[]
        for w in words1:
            word_count = Counter(w)
            if all(word_count[c] >= max_count[c] for c in max_count):
                res.append(w)


        return res