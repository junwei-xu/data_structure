#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/14 14:27
# description
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#  
#
# 例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
#
# 示例 1：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
#
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false

class Solution:
    # 矩阵搜索问题 想到 -> 深度优先搜索+剪枝
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:  # 索引越界 or 字符不匹配
                return False
            if k == len(word) - 1:  # 全部匹配
                return True
            board[i][j] = ''  # 标记当前矩阵元素，代表此元素已访问过，防止之后搜索时重复访问
            # 朝当前元素的 上、下、左、右 四个方向开启下层递归；只需找到一条可行路径就直接返回
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            # 还原当前矩阵元素
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
