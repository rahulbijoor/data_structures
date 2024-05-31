class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashtable={}
        for num in nums:
            if num in hashtable.keys():
                hashtable[num]=hashtable[num]+1
            else :
                hashtable[num]=1
            if hashtable[num] > len(nums)/2:
                return num
        return 0
            
        