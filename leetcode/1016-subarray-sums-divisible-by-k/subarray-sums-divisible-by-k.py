class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt=0
        sum=0
        ht={}
        ht[0]=1
        for num in nums:
            sum += num
            rem = sum % k
            if rem in ht.keys():
                cnt += ht[rem]
                ht[rem] += 1
            else:
                ht[rem]=1
            
        return cnt


        