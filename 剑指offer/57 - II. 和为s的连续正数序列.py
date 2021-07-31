#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/29 20:43
# description
# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

# 滑动窗口
# 也可以用公式计算（等差数列求和）
class Solution:
    def findContinuousSequence(self, target: int) -> list[list[int]]:
        i, j, s = 1, 2, 3
        res = []
        while i < j:
            if s > target:
                # 左边界向右
                s -= i
                i += 1
            elif s < target:
                # 右边界向左
                j += 1
                s += j
            else:
                res.append(list(range(i, j + 1)))
                # 找下一对
                s -= i
                i += 1
        return res
