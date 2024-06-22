# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

#U
#Time/Space
# Input size of 1

#M
#Binary Search

#P
#low = 1 and high= n
#
# mid of the element


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        result = n
        while low <= high:
            mid = low + (high-low)//2
            if isBadVersion(mid):
                result = mid
                high= mid-1
            else:
                low = mid + 1
        return result

