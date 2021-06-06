#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/5 21:59
# description 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
# 请找出数组中任意一个重复的数字
class Solution:
    # 不思考想到的 超时
    def blpj(self, nums: list[int]) -> int:
        dit = dict()
        for num in nums:
            if num in dit.keys():
                dit[num] += 1
            else:
                dit[num] = 1
        for k, v in dit.items():
            if v != 1:
                return k

    # 解法一：利用set
    def using_set(self, nums: list[int]) -> int:
        save = set()
        for num in nums:
            if num in save:
                return num
            else:
                save.add(num)
        return -1  # 随便什么

    # 解法二：原地交换
    def findRepeatNumber(self, nums: list[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:  # 如果在索引和值一致（萝卜在自己的坑里了）
                i += 1
                continue
            if nums[nums[i]] == nums[i]:  # 如果值所对应的位置已经有一样的了就返回（萝卜二号坑被占了）
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]  # 交换（萝卜找到自己的坑）
        return -1
