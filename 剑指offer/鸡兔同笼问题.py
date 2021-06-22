#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/22 20:49
# description
n = int(input())
l = list()
for k in range(n):
    inputNum = int(input())
    # 奇数
    if inputNum % 2 != 0:
        min = max = 0
    else:
        j = inputNum / 4
        i = inputNum % 4 / 2
        min = i + j
        # max
        max = inputNum / 2
    l += [(min, max)]

for a, b in l:
    print(a, b)
