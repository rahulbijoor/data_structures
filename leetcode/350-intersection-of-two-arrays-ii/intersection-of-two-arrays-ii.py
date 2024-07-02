class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ht1={}
        ht2={}
        result=[]
        for i in nums1:
            if i in ht1:
                ht1[i] += 1
            else:
                ht1[i] = 1
        for i in nums2:
            if i in ht2:
                ht2[i] += 1
            else:
                ht2[i] = 1
        for key,value in ht1.items():
            if key in ht2.keys():
                result += [key for i in range(min(ht1[key],ht2[key]))]
        
        return result