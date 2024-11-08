class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[i-1]^nums[i])
        
        mask = (1 << maximumBit) - 1
        ans=[]
        for i in range(len(nums)):
            prod = prefix[-i-1]
            ans.append( prod ^ mask)
        return ans