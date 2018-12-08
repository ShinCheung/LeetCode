# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集
# 说明：解集不能包含重复的子集
# 示例:
# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# 迭代思想
# 数组中只有一个数字时，返回空集合和数字本身，再新加一个数字时，将原先的所有子集加上新的数字，
# 就是包含新数字的子集，保留之前不包含新数字的子集。这两个子集直接相加就是新的所有子集。
# 一样地当数组长度不断增加，不断往原来子集上迭代新的集合即可。
class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])
        return res
    
    def subsets2(self, nums):
        res = [[]]
        while nums:
            x = nums.pop(0)
            for i in res[:]:
                res.append(i + [x])
        return res

print(Solution().subsets([1,2,3]))
print(Solution().subsets2([1,2,3]))
