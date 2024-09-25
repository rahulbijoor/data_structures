class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[1])
        prev_end = points[0][1]
        count = 0
        for i in range(1,len(points)):
            if prev_end >= points[i][0]:
                continue
            count += 1
            prev_end = points[i][1] 
        print(points)
        return count+1
