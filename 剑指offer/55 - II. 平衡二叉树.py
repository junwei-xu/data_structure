#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/27 21:37
# description 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
# 如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 从顶至底
# 先序遍历 + 判断深度
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
