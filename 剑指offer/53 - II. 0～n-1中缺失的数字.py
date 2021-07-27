#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/22 20:20
# description
# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
# 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
# 输入: [0,1,3]
# 输出: 2


# 排序数组中的搜索问题，首先想到 《二分法》 解决。
class Solution:
    # 缺失的数字等于 “右子数组(nums[i] != i )的首位元素” 对应的索引
    def missingNumber(self, nums: list[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i

    # 暴力破解
    def bl_missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
