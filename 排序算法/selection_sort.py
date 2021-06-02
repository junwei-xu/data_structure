#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/30 20:04
# description 选择排序
def selection_sort(data_list: list):
    """选择排序"""
    n = len(data_list)
    for i in range(n - 1):
        print('第%d次' % i, data_list)

        # 假定当前下标元素为最小值
        min_index = i
        # 找到实际最小值的下标
        for j in range(i + 1, n):
            if data_list[j] < data_list[min_index]:
                min_index = j
        # 交换
        if min_index != i:
            data_list[i], data_list[min_index] = data_list[min_index], data_list[i]


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(li)
    print(li)
