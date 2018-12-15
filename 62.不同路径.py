# 一个机器人位于一个 m x n 网格的左上角
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角,问总共有多少条不同的路径？
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 机器人一定会走m+n-2步，即从m+n-2中挑出m-1步向下走就行了
        res = 1
        for i in range(m, m+n-1):
            res *= i
            res //= i-m+1
        return res