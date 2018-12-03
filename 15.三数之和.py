# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
# 找出所有满足条件且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    # AC
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i] > nums[i-1]:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    res = nums[i] + nums[l] + nums[r]
                    if res == 0:
                        ans.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:   
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif res < 0:
                        l += 1
                    else:
                        r -= 1
        return ans

    # leetcode超时
    def threeSum_V2(self, nums):
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if res == 0:
                    sol = [nums[i], nums[l], nums[r]]
                    if sol not in ans:
                        ans.append(sol)
                    l += 1
                    r -= 1
                elif res < 0:
                    l += 1
                else:
                    r -= 1           
        return ans

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum_V2([-1, 0, 1, 2, -1, -4]))
