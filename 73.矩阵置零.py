# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
# 示例 1:
# 输入: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2:
# 输入: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
class Solution:
    def setZeroes(self, matrix):
        if not matrix:
            return
        rnum, cnum = len(matrix), len(matrix[0])
        r = [False for i in range(rnum)]
        c = [False for i in range(cnum)]
        # 遍历，把为0的地方置为True
        for i in range(rnum):
            for j in range(cnum):
                if matrix[i][j] == 0:
                    r[i] = True
                    c[j] = True
        # 再次遍历，把有0的行列置为0
        for i in range(rnum):
            for j in range(cnum):
                if r[i] or c[j]:
                    matrix[i][j] = 0
        return matrix

print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
