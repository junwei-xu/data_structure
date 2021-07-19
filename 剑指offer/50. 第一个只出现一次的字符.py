#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/19 22:36
# description
# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
import collections


class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = not i in dic  # 直接赋值boolean值
        for i in s:
            if dic[i]:
                return i
        return " "

    def ordered_firstUniqChar(self, s: str) -> str:
        # dic = collections.OrderedDict()  # Python 3.6 后，默认字典就是有序的，因此无需使用 OrderedDict()
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v:
                return k
        return ' '
