#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/31 18:11
# description
# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

#        分治思想 五张牌构成顺子的充分条件需要满足
#       1. 不重复 使用Set去重
#       2. max - min < 5 最大牌值 减去 最小牌值 小于5 且跳过大小王
class Solution:
    def isStraight(self, nums: list[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14  # 最大牌和最小牌  min和max的初始值是两个边界值[0, 13]
        for num in nums:
            if num == 0:
                continue
            ma = max(ma, num)
            mi = min(mi, num)
            if num in repeat:
                return False
            repeat.add(num)
        return ma - mi < 5
