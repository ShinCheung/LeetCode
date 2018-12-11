# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
# 其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
# 示例:
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题
# 分两步做:
# 第一步求所有小于当前i的乘积，从左到右循环，用一个变量维护这个乘积，
# 第二步求所有大于当前i的乘积，从右到左循环，同样用一个变量维护这个乘积
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for _ in range(n)]
        
        product_lt = 1
        for i in range(1, n):
            product_lt *= nums[i - 1]
            res[i] *= product_lt
        
        product_gt = 1
        for i in range(n - 2, -1, -1):
            product_gt *= nums[i + 1]
            res[i] *= product_gt
        
        return res