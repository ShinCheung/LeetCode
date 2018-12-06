# 计算每个位置上可以盛放的水，累加起来。

class Solution:
    def trap(self, height):
        if not height:
            return 0
        maxl = maxr = res = 0
        l, r = 0, len(height) - 1
        while l <= r:
            if height[l] < height[r]:
                maxl = max(maxl, height[l])
                res += maxl - height[l]
                l += 1
            else:
                maxr = max(maxr, height[r])
                res += maxr - height[r]
                r -= 1
        return res