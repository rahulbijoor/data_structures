class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
        # Calculate the carry
            carry = (a & b) << 1 & MASK
            # Calculate the sum without carry
            a = ( a ^ b ) & MASK
            # Update b to carry
            b = carry
        return a if a <= MAX_INT else ~(a ^ MASK)