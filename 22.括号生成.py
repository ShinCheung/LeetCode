# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 例如，给出 n = 3，生成结果为：
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        # 否则按照左右括号剩余个数判断生成括号
        self.helpler(n, n, '', res)
        return res
    
    # 生成括号组成的函数
    # 如果左括号有剩余即 left>0 则可以添加左括号
    # 如果右括号剩余数大于左括号剩余数 即right>left 则可以添加右括号
    def helpler(self, l, r, item, res):
        if l == r == 0:
            res.append(item)
        if l > 0:
            self.helpler(l - 1, r, item + '(', res)
        if r > l:
            self.helpler(l, r - 1, item + ')', res)
