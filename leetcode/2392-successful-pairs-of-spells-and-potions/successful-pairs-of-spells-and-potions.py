class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        arr = [ math.ceil( success/potion ) for potion in potions ]
        arr.sort()

        result=[]
        for sp in spells:
            l, r, M = 0, len(arr)-1, 0
            while l <= r:
                m = l + (r-l)//2
                if arr[m] <= sp:
                    l = m + 1
                    M = l
                else:
                    r = m -1
            result.append(M)
        return result