class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ht={}
        minMax=0
        count = 0
        for num in nums:
            if num in ht.keys():
                ht[num] += 1
            else:
                ht[num] = 1
        for num in nums:
            if num in ht.keys() and k-num in ht.keys():
                if num != k/2:
                    count += min(ht[num],ht[k-num])
                else:
                    count += floor(ht[num]/2)
                del ht[num]
                if num != k-num:
                    del ht[k-num]

        
        return count

