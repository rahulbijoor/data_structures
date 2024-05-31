class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ht={}
        for num in nums:
            if num in ht.keys():
                ht[num]+=1
            else:
                ht[num]=1
        l=[]
        for key in ht.keys():
                if ht[key] == 1:
                    l.append(key)
        return l