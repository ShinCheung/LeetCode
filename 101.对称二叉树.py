# 给定一个二叉树，检查它是否是镜像对称的
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

#     1
#    / \
#   2   2
#    \   \
#    3    3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :tyre root: TreeNode
        :rtyre: bool
        """
        if root:
            return self.digui(root.left, root.right)
        else:
            return True
    
    def digui(self, l, r):
        if l and r:
            return l.val == r.val and self.digui(l.left, r.right) and self.digui(l.right, r.left)
        else:
            return not l and not r
        