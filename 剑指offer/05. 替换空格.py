#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/6 9:51
# description 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
class Solution:
    # 解法一：偷懒解法
    def tl(self, s: str) -> str:
        return s.replace(' ', '%20')

    # 解法二：老实解法
    def replaceSpace(self, s: str) -> str:
        res = []
        for char in s:
            if char == ' ':
                res.append('%20')
            else:
                res.append(char)
        return "".join(res)  # 注意join的用法
