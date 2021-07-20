#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/20 21:47
# description 统计一个数字在排序数组中出现的次数。
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2

class Solution:
    # 二分法 确定重复数组的左右边界 right - left -1 即为重复次数
    def search(self, nums: [int], target: int) -> int:
        # 搜索右边界 right
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1
        right = i

        # 若数组中无 target ，则提前返回
        if j >= 0 and nums[j] != target:
            return 0

        # 搜索左边界 left
        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:  # 这里相当于往左
                i = m + 1
            else:
                j = m - 1
        left = j

        return right - left - 1
