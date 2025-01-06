class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left = [0]*len(boxes)
        right = [0]*len(boxes)
        balls = 0
        moves = 0
        l = len(boxes)
        if boxes[l-1]=='1':
            balls = 1 
        for i in range(len(boxes)-2,-1,-1):
            left[i]=balls+left[i+1]
            if boxes[i] == '1':
                balls += 1
        balls = 0
        if boxes[0] == "1":
            balls = 1
        for i in range(1,len(boxes)):
            right[i]=balls+right[i-1]
            if boxes[i] == '1':
                balls += 1
        return [left[i]+right[i] for i in range(l)]