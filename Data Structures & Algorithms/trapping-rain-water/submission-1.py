class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        i = 0
        j = len(height) - 1
        leftWall = height[i]
        rightWall = height[j]
        while i < j:
            if leftWall < rightWall:
                i += 1
                leftWall = max(leftWall, height[i])
                water += leftWall - height[i]
            else:
                j -= 1
                rightWall = max(rightWall, height[j])
                water += rightWall - height[j]
        return water