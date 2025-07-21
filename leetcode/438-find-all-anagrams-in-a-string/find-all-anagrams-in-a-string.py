from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        n = len(p)
        freq1 = Counter(p)
        window = Counter()

        for i in range(len(s)):
            window[s[i]] += 1
            if i >= n:
                left_char = s[i-n]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
            if window == freq1:
                res.append(i-n+1)
        return res