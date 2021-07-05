#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/4 9:46
# description
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root:
            return []

        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            tmp = []

            for _ in range(len(queue)):  # 判断当前层结点数
                node = queue.popleft()
                tmp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res
