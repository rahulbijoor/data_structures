class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = bin(n)[2:].zfill(32)
        rev_str=""
        right = len(binary_string)-1
        while right >= 0:
            rev_str += binary_string[right]
            right -= 1

        return int(rev_str, 2)   
        