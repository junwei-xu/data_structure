#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/29 19:59
# description 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

# 这道题主要是递增排序的 所以可以用双指针对撞 o(1)复杂度
# 非排序的只能用HasMap遍历 o(n)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] + nums[j] < target:
                i += 1
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                return [nums[i], nums[j]]
        return []
