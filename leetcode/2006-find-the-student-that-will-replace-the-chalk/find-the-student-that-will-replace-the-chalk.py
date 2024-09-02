class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        l = len(chalk)
        i = 0
        k = k%sum(chalk) 
        while k >= 0:
            k -= chalk[i]
            if k < 0:
                return i
            i = (i+1)%l
        
        return i