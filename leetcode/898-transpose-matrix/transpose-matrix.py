class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        newMatrix=[]

        for i in range(len(matrix[0])):

            newMatrix.append([])
            for j in range(len(matrix)):
                newMatrix[i].append(matrix[j][i])
        
        
        return newMatrix