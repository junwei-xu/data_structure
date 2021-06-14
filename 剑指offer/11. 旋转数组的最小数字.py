#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/13 16:32
# description
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
#
# 示例 1：
#
# 输入：[3,4,5,1,2]
# 输出：1
# 示例 2：
#
# 输入：[2,2,2,0,1]
# 输出：0

class Solution:

    # 暴力破解
    def blpj_minArray(self, numbers: list[int]) -> int:
        target = 0

        while target < len(numbers) - 1:
            if numbers[target] <= numbers[target + 1]:
                target += 1
            else:
                return numbers[target + 1]
        else:
            return numbers[0]

    # 二分法
    def minArray(self, numbers: list[int]) -> int:
        left, right = 0, len(numbers) - 1

        while left < right:  # left=right 退出循环
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:  # 最小值在mid后面
                left = mid + 1
            elif numbers[mid] < numbers[right]:  # 最小值在mid前面
                right = mid
            else:  # 有重复数字
                right -= 1
        return numbers[left]
