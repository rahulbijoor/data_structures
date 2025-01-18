class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        first = 0
        last = 0
        for d in derived:
            if d == 1:
                last = ~last
            else:
                last = last
        return first == last