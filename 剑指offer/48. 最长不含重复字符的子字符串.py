#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/13 19:42
# description
#
# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

# 想象成一个滑动的窗口（滑轨）
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, left = {}, 0, -1
        for right in range(len(s)):
            if s[right] in dic:
                left = max(dic[s[right]], left)  # 更新左指针,保证区间 [left + 1, right]内无重复字符且最大  !注意点
            dic[s[right]] = right  # 哈希表记录
            res = max(res, right - left)  # 更新结果
        return res
