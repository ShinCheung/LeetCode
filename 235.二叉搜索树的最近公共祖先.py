# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
#         _______6______
#        /              \
#     ___2__          ___8__
#    /      \        /      \
#    0      _4       7       9
#          /  \
#          3   5
# 示例 1:
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# 输出: 6 
# 解释: 节点 2 和节点 8 的最近公共祖先是 6。
# 示例 2:
# 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# 输出: 2
# 解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉搜索树中。

# 思想是二叉搜索树的性质，小的在左，大的在右，从根结点开始与p和q进行比较，就能判断p和q是在当前节点的某一侧还是两侧了。
# 如果在两侧，则此节点就是他们的最近公共祖先，如果在一侧，则递归到这一侧的节点重新比较。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
