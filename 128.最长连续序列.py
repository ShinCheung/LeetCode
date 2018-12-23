# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        tmp = res = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] - 1 == nums[i-1]:
                tmp += 1
            else:
                res = max(res, tmp)
                tmp = 1
        return max(res, tmp)

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))