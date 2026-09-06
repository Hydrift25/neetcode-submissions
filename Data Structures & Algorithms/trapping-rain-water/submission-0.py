class Solution:
    def trap(self, height: List[int]) -> int:
        leftWalls = []
        rightWalls = [0] * len(height)
        lmax = 0
        for x in range(len(height)):
            leftWalls.append(lmax)
            if height[x] > lmax:
                lmax = height[x]
        rmax = 0
        for y in range(len(height)):
            rightWalls[-y-1] = rmax
            if height[-y-1] > rmax:
                rmax = height[-y-1]
        return sum([max(min(leftWalls[i], rightWalls[i]) - height[i], 0) for i in range(len(height))])