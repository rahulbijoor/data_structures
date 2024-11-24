class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = len(citations)
        maxVal = 0
        
        for i in range(1, l + 1): 
            count = 0
            
            for j in range(l): 
                if citations[j] >= i:
                    count += 1
            
            if count >= i:  
                maxVal = i  
            else:
                break
        
        return maxVal

