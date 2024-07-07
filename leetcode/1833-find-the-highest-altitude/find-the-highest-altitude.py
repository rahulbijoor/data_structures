class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        Sum=0
        maxAlt=0
        for num in gain:
            Sum+=num
            maxAlt=max(maxAlt,Sum)
        return maxAlt