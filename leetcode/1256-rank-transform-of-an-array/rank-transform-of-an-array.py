class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = sorted(arr)
        hash = {}
        count = 0
        for a in arr2:
            if a not in hash.keys():
                hash[a] = count+1
                count += 1
        result = []
        for a in arr:
            result.append(hash[a])
        return result