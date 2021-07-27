#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/27 21:04
# description 输入一棵二叉树的根节点，求该树的深度。
# 从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 后序遍历（DFS）
    # 树的后序遍历 / 深度优先搜索往往利用 递归 或 栈 实现
    def dfs_maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.dfs_maxDepth(root.left), self.dfs_maxDepth(root.right)) + 1

    # 层序遍历（BFS）
    # 树的层序遍历 / 广度优先搜索往往利用 队列 实现
    def bfs_maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue, res = [root], 0
        while queue:
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            res += 1
        return res
