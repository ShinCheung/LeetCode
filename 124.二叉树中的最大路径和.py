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
# 思路：递归
# 对于每一个根节点来说，
# 经过该点的最大路径是max(该点的值，该点的值加左子树的最大路径，该点的值加右子树的最大路径，该点的值加左右子树最大路径的和)，
# 得到的应该是这些值中的最大值，但是当递归作为子树的最大值返回给父节点时，
# 我们返回的应该是max(该点的值，该点的值加左子树的最大路径，该点的值加右子树的最大路径)，
# 不应该加上左右节点之和，因为这样的话，得到的就是如果作为子树返回的是，
# 如果按照左中右结果返回，那么从根节点必须通过回溯才能走完这个子树，这一点需要注意。
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
