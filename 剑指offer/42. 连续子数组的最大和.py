#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/19 22:26
# description
# 输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
#
# 要求时间复杂度为O(n)。
#
#
# 示例1:
#
# 输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释:连续子数组[4,-1,2,1] 的和最大，为6。
#
class Solution:
    # 动态规划
    # 设动态规划列表 dp ，dp[i] 代表以元素 《nums[i] 为结尾》的连续子数组最大和
    #  若dp[i−1]≤0 ，说明dp[i−1] 对dp[i] 产生负贡献，即 dp[i-1] + nums[i]还不如 nums[i]本身大
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
