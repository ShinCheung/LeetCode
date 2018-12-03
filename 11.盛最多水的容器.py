# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
# 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 示例:
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49

class Solution(object):
    '''
    题意:任取两个a[i]、a[j] 使得min(a[i], a[j]) * abs(i - j)最大化
    用两个指针从两侧向中间扫描，每次移动数值较小的指针，用反证法可以证明
    总是可以得到最优答案
    '''
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                area = height[left] * (right - left)
                left += 1
            else:
                area = height[right] * (right - left)
                right -= 1
            ans = max(ans, area) 
        return ans
        
        # water = 0
        # i = 0
        # j = len(height) - 1
        # while i < j:
        #     h = min(height[i], height[j])
        #     water = max(water, (j - i) * h)
        #     while height[i] <= h and i < j:
        #         i += 1
        #     while height[j] <= h and i < j:
        #         j -= 1
        # return water
