class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        min_repeats = (len(b) + len(a) - 1) // len(a)
        
        # Check for both min_repeats and min_repeats + 1
        for i in range(min_repeats, min_repeats + 2):
            if b in a * i:
                return i
        
        return -1
       
        