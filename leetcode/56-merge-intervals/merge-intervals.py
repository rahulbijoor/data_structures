class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack =[]
        intervals.sort()
        for interval in intervals:
            if not stack or stack[-1][-1] < interval[0]:
                stack.append(interval)
            else:
                top = stack.pop()
                max_end = max(top[-1],interval[-1])
                new_interval = [top[0],max_end]
                stack.append(new_interval)
        return stack
