class Solution:
    def mySqrt(self, x: int) -> int:
        low=0
        high=x
        result=x
        while low <= high:
            mid = low + (high-low)//2
            if mid*mid < x:
                result=mid
                low = mid+1
            elif mid*mid > x:
                high = mid-1
            else:
                return mid
        return result


        