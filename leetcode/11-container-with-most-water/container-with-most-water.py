class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_w=0
        l = 0
        r = len(height)-1
        while l < r:
            wl = (r-l)* min(height[l],height[r])
            max_w = max(max_w,wl)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_w
