#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/3 18:28
# description
# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R:  # 当 L 和 R 同时越过叶节点
                return True
            if not L or not R or L.val != R.val:  # 当 L 或 R 中只有一个越过叶节点;当节点L值 != 节点R值
                return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return recur(root.left, root.right) if root else True
