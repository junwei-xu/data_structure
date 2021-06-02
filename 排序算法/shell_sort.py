#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/31 22:33
# description 希尔排序
# 把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
# 随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止
def shell_sort(data_list: list):
    n = len(data_list)
    # 初始步长
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and data_list[j - gap] > data_list[j]:
                data_list[j - gap], data_list[j] = data_list[j], data_list[j - gap]
                i -= gap
        gap = gap // 2


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(li)
    print(li)
