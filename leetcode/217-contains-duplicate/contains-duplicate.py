class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ht = set()
        for num in nums:
            if num in ht:
                return True
            else:
                ht.add(num)
        return False

        