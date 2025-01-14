class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        setA = set()
        setB = set()
        count = 0
        res =[]
        for i in range(len(A)):
            if A[i] in setB:
                count += 1
            if B[i] in setA:
                count += 1
            if A[i] == B[i]:
                count+= 1
            setA.add(A[i])
            setB.add(B[i])
            res.append(count)
        return res
