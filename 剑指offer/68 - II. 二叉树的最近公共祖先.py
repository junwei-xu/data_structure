#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/8/1 15:52
# description 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:  # left 为空 ，right不为空
            return right
        if not right:  # left 不为空 ， right为空
            return left
        return root  # left和right 同时不为空 异侧
