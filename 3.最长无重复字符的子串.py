# 给定一个字符串，找出不含有重复字符的最长子串的长度。
# 示例 1:
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 无重复字符的最长子串是 "abc"，其长度为 3。
# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 无重复字符的最长子串是 "b"，其长度为 1。
# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 无重复字符的最长子串是 "wke"，其长度为 3。
#      请注意，答案必须是一个子串，"pwke" 是一个子序列 而不是子串。

class Solution:
    # 法一
    def lengthOfLongestSubstring(self, s):
        # 开始坐标和最大长度都是0
        start = maxlen = 0
        # 设置一个空字典
        dt = {}
        # 写一个for循环，循环s的长度
        for i in range(len(s)):
            # 判断s[i]是否在字典当中并且开始坐标小于字典中对应s[i]的值,也就是s[i]中的值一定要在start后面
            if s[i] in dt and start <= dt[s[i]]: 
                # 如果满足上面的条件,start等于当前的字符串i位置的值+1
                start = dt[s[i]] + 1
            else:
                # 否则的话，返回最大的长度,maxlen,或者当前的i-起始值+1
                maxlen = max(maxlen,i - start + 1) 
            # 把dt[s[i]]重置为i
            dt[s[i]] = i
        return maxlen
    
    # 简化优化法一
    # def lengthOfLongestSubstring(self, s):
    #     maxlen = 0
    #     start = 0
    #     dt = {}
    #     for i,c in enumerate(s):
    #         if c in dt:
    #             start = max(start,dt[c]+1)
    #         maxlen = max(maxlen,i-start+1)   
    #         dt[c] = i
    #     return maxlen

    # 获取字符串
    # def findstr(str):
    #     start = maxlength = 0
    #     a = {}
    #     begin = end = 0
    #     for i in range(len(str)):
    #         if str[i] in a and start <= a[str[i]]:
    #             start = a[str[i]] + 1
    #         else:
    #             if maxlength <= i-start+1:
    #                 begin = start
    #                 end = i
    #             maxlength = max(maxlength, i-start+1)
    #         a[str[i]] = i
    #     return str[begin:end+1]
print(Solution().lengthOfLongestSubstring('12345678980'))
