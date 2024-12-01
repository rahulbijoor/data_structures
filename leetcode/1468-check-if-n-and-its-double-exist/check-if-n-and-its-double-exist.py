class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s =set()
        for i in range(len(arr)):
            if arr[i]*2 in s or arr[i]/2 in s:
                return True
            s.add(arr[i])
        return False