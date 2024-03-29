#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/2 21:47
# description 二分查找
# 适用于有序的序列
def binary_search(data_list: list, search_item: int):
    if len(data_list) == 0:
        return False
    else:
        mid = len(data_list) // 2
        if data_list[mid] == search_item:
            return mid
        else:
            if search_item < data_list[mid]:
                return binary_search(data_list[:mid], search_item)
            else:
                return binary_search(data_list[mid + 1:], search_item)


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, 66]
    print(binary_search(testlist, 3))
    print(binary_search(testlist, 13))
