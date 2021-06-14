#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/6 20:05
# description
# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

class Solution:
    # 普通递归法，超时
    def dg_fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return (self.dg_fib(n - 1) + self.dg_fib(n - 2)) % 1000000007

    # 最优解：动态规划
    def fib(self, n: int) -> int:
        # if n == 0 or n == 1:
        #     return n
        # else:
        #     # 从下往上算
        #     dp = [0, 1]
        #     for i in range(2, n + 1):
        #         dp_tmp = (dp[i - 1] + dp[i - 2]) % 1000000007
        #         dp.append(dp_tmp)
        #     return dp[n]

        a, b = 0, 1
        # 同上一个意思，消耗更少的空间
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007