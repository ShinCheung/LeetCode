# 给定一个非空二叉树，返回其最大路径和。
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 示例 1:
# 输入: [1,2,3]

#        1
#       / \
#      2   3
# 输出: 6
# 示例 2:
# 输入: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7
# 输出: 42
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nodeSum = []
        def findSum(root):
            if not root:
                return 0
            left = findSum(root.left)
            right = findSum(root.right)
            nodeVal = max(root.val, root.val+left, root.val+right, root.val + left + right)
            nodeSum.append(nodeVal)
            return max(root.val, root.val + left, root.val + right)
          
        findSum(root)
        return max(nodeSum)