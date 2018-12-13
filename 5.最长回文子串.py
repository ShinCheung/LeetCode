# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
# 输入: "cbbd"
# 输出: "bb"
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        while True:
            for i in range(len(s) - l + 1):
                res = s[i:i+l]
                if res == res[::-1]:
                    return res
            l -= 1