class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxWater = 0
        while left < right:
            currentWater = (right-left)*min(height[left],height[right])
            maxWater = max(maxWater, currentWater)
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        
        return maxWater