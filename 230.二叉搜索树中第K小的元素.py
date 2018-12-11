# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
# 示例 1:
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 1
# 示例 2:
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 也是运用了stack，既然是BST，那么in order traversal肯定就是从小到大排列的。
# 第一次pop就是最小的数字，第二次就是第二小的数字，以此类推。
# 用一个counter记录pop的次数，直到counter == k为止，所pop的数字就是要找的
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        n = 0
        stack = []
        while root or stack != []:
            while root:
                stack.append(root)
                root = root.left
            if stack != []:
                root = stack.pop()
                n += 1
                if n == k:
                    return root.val
                root = root.right
        return 

    def kthSmallest2(self, root, k):
        def inorderTraversal(root):
            if not root:
                return []
            res = []
            res.extend(inorderTraversal(root.left))
            res.append(root.val)
            res.extend(inorderTraversal(root.right))
            return res
        return inorderTraversal(root)[k - 1]