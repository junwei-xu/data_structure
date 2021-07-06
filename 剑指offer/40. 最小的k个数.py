#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/6 9:29
# description
# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

class Solution:
    def getLeastNumbers(self, arr: list[int], k: int) -> list[int]:
        if k >= len(arr):
            return arr

        def partition(array, left, right):
            pivot = array[left]
            while left < right:
                while left < right and array[right] >= pivot:
                    right -= 1
                array[left] = array[right]
                while left < right and array[left] < pivot:
                    left += 1
                array[right] = array[left]
            array[left] = pivot
            return left

        # 如果某次哨兵划分后 基准数正好是第 k+1小的数字 ，那么此时基准数左边的所有数字便是题目所求的 最小的 k 个数
        def quick_sort(array, left, right, k):
            if left < right:
                pivot_index = partition(array, left, right)
                if pivot_index < k:  # 还不够，右边再排一下
                    quick_sort(array, pivot_index + 1, right, k)
                else:  # 多了，左边再排一下
                    quick_sort(array, left, pivot_index - 1, k)

        quick_sort(arr, 0, len(arr) - 1, k)
        return arr[:k]
