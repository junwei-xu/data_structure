#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/31 13:59
# description 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
# 为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。
# 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
# 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

class Solution:
    # 双指针
    def reverseWords(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':  # 搜索首个空格
                i -= 1
            res.append(s[i + 1:j + 1])  # 添加单词
            while s[i] == ' ':  # 跳过单词间空格
                i -= 1
            j = i  # j 指向下个单词的尾字符
        return ' '.join(res)  # 拼接并返回

    # 分割 + 倒序
    def reverseWords2(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        strs = s.split()  # 分割字符串,split() 方法将单词间的 “多个空格看作一个空格”
        strs.reverse()  # 翻转单词列表
        return ' '.join(strs)  # 拼接为字符串并返回
