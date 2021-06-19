#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/16 13:59
# description
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#
# 示例：
#
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。

class Solution:
    # 辅助数组
    def fzsj_exchange(self, nums: list[int]) -> list[int]:
        js = []
        os = []
        for i in nums:
            if i % 2 != 0:
                js.append(i)
            else:
                os.append(i)
        return js + os

    # 双指针
    def szz_exchange(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] % 2 == 1:
                left += 1
                continue
            elif nums[right] % 2 == 0:
                right -= 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
        return nums

    # 快慢双指针 龟兔赛跑
    def km_exchange(self, nums: list[int]) -> list[int]:
        left, right = 0, 0
        while right < len(nums):
            # 如果快指针指向奇数，则交换到前面，且慢指针前移
            if nums[right] % 2 == 1:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            # 快指针始终前移
            right += 1
        return nums