class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l = len(flowerbed)
        if n == 0:
            return True
        if l == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            else:
                return False
                
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
         
        for i in range(1,l-1):
            if flowerbed[i-1] == 0 and flowerbed[i]== 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
        
        if flowerbed[l-2] == 0 and flowerbed[l-1] == 0:
            flowerbed[l-1] = 1
            n -= 1

        if n <= 0:
            return True
        return False

            
        