# 给定一个 n × n 的二维矩阵表示一个图像
# 将图像顺时针旋转 90 度
# 给定 matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # matrix[:] = list(zip(*matrix[::-1]))
        return list(zip(*matrix[::-1]))

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(Solution().rotate(a))