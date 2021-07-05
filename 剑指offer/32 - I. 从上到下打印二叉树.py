#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/4 9:13
# description
# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。


# Definition for a binary tree node.
import collections
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 两个数组 保存cur_nodes和next_nodes
    def lgsz_levelOrder(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        cur_nodes = [root]
        next_nodes = []

        res = []
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                res.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            # 继续遍历下一层
            cur_nodes = next_nodes
            next_nodes = []
        return res

    # 双端队列
    def levelOrder(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        # 双端队列
        res, queue = [], collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            res.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res