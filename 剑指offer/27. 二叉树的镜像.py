#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/20 14:21
# description
# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。
#
# 例如输入：
#
#   4
#  /  \
#  2   7
# / \  / \
# 1  3 6  9
# 镜像输出：
#
#   4
#  /  \
#  7   2
# / \  / \
# 9  6 3 1
#
#
# 示例 1：
#
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归法
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = root.right, root.left
            self.mirrorTree(root.left)
            self.mirrorTree(root.right)
        return root

    # 辅助栈or队列
    def fzz_mirrorTree(self, root: TreeNode):
        if not root:
            return
        stack = [root]
        while stack:
            # 出栈： 记为 node
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            # 交换
            node.left, node.right = node.right, node.left
        return root
