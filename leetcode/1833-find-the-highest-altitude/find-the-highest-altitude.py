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
            if maxAlt < Sum:
                maxAlt= Sum
        return maxAlt