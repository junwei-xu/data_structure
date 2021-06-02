#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/30 19:34
# description 冒泡排序

def bubble_sort(data_list: list):
    """冒泡排序"""
    n = len(data_list)
    for i in range(n - 1):
        print('第%d次' % i, data_list)
        # 和后面的依次比对，直到最大值到最后一位
        for j in range(n - 1 - i):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
    return data_list


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(li)
    print(li)
