class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rowLength, colLength = len(image), len(image[0])
        for i in range(rowLength):
            image[i] = image[i][::-1]

            for j in range(colLength):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        
        return image