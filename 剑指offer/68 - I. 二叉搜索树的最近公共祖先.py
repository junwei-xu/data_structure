#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/8/1 11:19
# description 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 二叉搜索树：左子树上所有结点的值均小于它的根结点的值；右子树上所有结点的值均大于它的根结点的值
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if root.val < p.val and root.val < q.val:  # p,q都在右子树中
                root = root.right
            elif root.val > p.val and root.val > q.val:  # p,q都在左子树中
                root = root.left
            else:
                break
        return root

    # 递归
    def dg_lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
