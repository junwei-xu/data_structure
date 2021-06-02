#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/30 20:10
# description 插入排序
# 每次挑选下一个元素插入已经排序的数组中,初始时已排序数组只有一个元素
def insertion_sort(data_list: list):
    """插入排序"""
    n = len(data_list)
    for i in range(1, n):
        print('第%d次' % i, data_list)

        # 保存当前位置的值(转移过程中可能会被覆盖)
        value = data_list[i]
        # 找到合适的位置,使前面的数组[0,i]有序
        pos = i
        while pos > 0 and value < data_list[pos - 1]:
            data_list[pos] = data_list[pos - 1]
            pos -= 1
        # 插进去
        data_list[pos] = value


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(li)
    print(li)
