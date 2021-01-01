# Leetcode #42, Hard, Trapping Rain Water
class Solution:
    def trap(self, height):

        n = len(height)
        if n <= 2: return 0

        while height[0] == 0:
            del height[0]
        while height[-1] == 0:
            del height[-1]

        n = len(height)
        if n <= 2: return 0

        water = 0
        for i in range(1, n - 1):
            left_max = max(height[0:i])
            right_max = max(height[i + 1:])
            level = min(left_max, right_max)
            if level > height[i]:
                water += level - height[i]
        return water

sln = Solution()
# print(sln.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sln.trap([2, 0,0,3,0,3]))