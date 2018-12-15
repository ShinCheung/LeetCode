# 给定一个二叉树，返回它的中序 遍历。
# 示例:
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 输出: [1,3,2]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        if root.left:
            res += self.inorderTraversal(root.left)
            # res.extend(self.inorderTraversal(root.left))
        if root.val:
            res.append(root.val)
        if root.right:
            res += self.inorderTraversal(root.right)
            # res.extend(self.inorderTraversal(root.right))
        return res
