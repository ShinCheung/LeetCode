# 给定一个二叉树，找出其最小深度
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量
# 说明: 叶子节点是指没有子节点的节点
# 示例:
# 给定二叉树 [3,9,20,null,null,15,7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2
# 分治法，分成以下四种情况:
# 1.当前节点有左右子树，分别计算左右子树的minimum depth，返回其中最小值 + 1
# 2.当前节点只有左子树，返回左子树的minimum depth + 1
# 3.当前节点只有右子树，返回右子树的minimum depth + 1
# 4.当前节点没有左右子树（叶子节点），返回1

# 分析之后，可发现2，3，4可归纳成一条规律。总体的算法如下:
# 1.递归的出口：当前为None，返回0
# 2.分别计算左右子树的minimum depth, 记为leftDepth 和 rightDepth
# 3.若当前节点有左右子树，返回min(leftDepth, rightDepth) + 1, 否则返回max(leftDepth, rightDepth) + 1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        lh = self.minDepth(root.left)
        rh = self.minDepth(root.right)
        if root.left and root.right:
            return min(lh, rh) + 1
        else:
            return max(lh, rh) + 1
