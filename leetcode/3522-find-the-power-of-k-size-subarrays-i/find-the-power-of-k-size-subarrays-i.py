class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        res = []
        for i in range(l-k+1):
            isConsecutive = True
            for  j in range(i,i+k-1):
                if nums[j] != nums[j+1]-1:
                    isConsecutive = False
                    break
            
            if isConsecutive:
                res.append(nums[i+k-1])
            else:
                res.append(-1)
        
        return res