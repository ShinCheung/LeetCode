# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 用index追踪level是奇数层还是偶数层，在value加入奇数层list的时候，用insert实现即时反转
# 而不是在value全部append之后统一反转
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        queue = [root]
        res = []
        index = 1
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if index % 2 != 0:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            index += 1
            res.append(level)
        return res