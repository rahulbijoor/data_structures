class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalSum = 0
        minAbsVal = float("inf")
        negativeCount = 0

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                totalSum += abs(matrix[row][col])
                if matrix[row][col] < 0:
                    negativeCount += 1
                minAbsVal = min(minAbsVal,abs(matrix[row][col]) )

        if negativeCount % 2 == 1:
            totalSum -= (2*minAbsVal)
        
        return totalSum