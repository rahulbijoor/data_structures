class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ht={}
        
        for i in range(0,len(heights)):
            ht[heights[i]] = names[i]
        
        heights.sort(reverse = True)
        for i in range(0,len(heights)):
            names[i] = ht[heights[i]]
        
        return names
