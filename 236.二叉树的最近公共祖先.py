# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#         _______3______
#        /              \
#     ___5__          ___1__
#    /      \        /      \
#    6      _2       0       8
#          /  \
#          7   4
# 示例 1:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例 2:
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。
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
        # p & 下面有q => p
        # q & 下面有p => q
        # p & 下面啥都没有 => p
        # q & 下面啥都有 => q
        if not root:
            return
        
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # p 和 q 一边一个
        if left and right: 
            return root
        
        # 左子树有一个点或者左子树有LCA
        if left:
            return left
        
        # 右子树有一个点或者右子树有LCA
        if right:
            return right
        
        # 左右子树啥都没有
        return