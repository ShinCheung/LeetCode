# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
# 示例:
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：所有输入均为小写字母。不考虑答案输出的顺序。
# 思路：当且仅当它们的排序字符串相等时，两个字符串是字母异位词。

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for s in strs:
            res[tuple(sorted(s))].append(s)
        return list(res.values())

test = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(test))