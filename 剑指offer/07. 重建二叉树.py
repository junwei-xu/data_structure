#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/6 10:47
# description
# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:

        def rebuild(root, left, right):  # root->preorder的位置  left,right -> inorder的位置
            if left > right:
                return
            node = TreeNode(preorder[root])

            # 这个地方可以用字典优化查询
            flag = 0
            for i, v in enumerate(inorder):  # 找到inorder中root的位置
                if v == preorder[root]:
                    flag = i

            node.left = rebuild(root + 1, left, flag - 1)  # 左子树
            node.right = rebuild(flag - left + root + 1, flag + 1, right)  # 右子树

            return node

        return rebuild(0, 0, len(preorder) - 1)
