#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/6 8:47
# description
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

class Solution:
    # 解法一：哈希表
    def hash_majorityElement(self, nums: list[int]) -> int:
        dic = {}
        for i in nums:
            if dic.get(i):
                dic[i] += 1
            else:
                dic[i] = 1
        ls = sorted(dic.items(), key=lambda item: item[1], reverse=True)  # 得到的是 [()]
        return ls[0][0]

    # 解法二： 排序法 中间的一定为众数
    def px_majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    # 解法三 摩尔投票法
    def vote_majorityElement(self, nums: list[int]) -> int:
        votes = 0
        x = 0
        for num in nums:  # 每一个人都要出来挑战
            if votes == 0:  # 擂台上没人 选一个出来当擂主 x就是擂主  votes就是人数
                x = num
            votes += 1 if num == x else -1  # 如果是自己人就站着呗 如果不是 就同归于尽
        return x
