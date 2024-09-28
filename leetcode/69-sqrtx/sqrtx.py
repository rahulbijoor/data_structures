class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:  # Handle cases for 0 and 1
            return x
        
        left, right = 1, x
        
        while left < right:
            mid = (left + right) // 2
            if mid * mid == x:  # Exact square root found
                return mid
            elif mid * mid < x:
                left = mid + 1  # Move to the right half
            else:
                right = mid  # Move to the left half
        
        return right - 1  # The largest integer whose square is <= x

