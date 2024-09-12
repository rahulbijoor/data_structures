class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        allow = set(allowed)
        for w in words:
            for c in w:
                if c not in allow:
                    count += 1
                    break

        return  len(words) - count
