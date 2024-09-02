class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        result=[]
        if m*n != l:
            return []
        index = 0
        while m > 0:
            row = [original[index + i] for i in range(n)]
            index = index + n
            m -= 1
            result.append(row)
        return result


        