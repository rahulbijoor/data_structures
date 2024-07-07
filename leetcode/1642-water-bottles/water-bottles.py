class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        result=numBottles
        
        while numBottles >= numExchange:
            rem=numBottles%numExchange
            result+=numBottles/numExchange
            numBottles=(numBottles/numExchange) + rem

        return result