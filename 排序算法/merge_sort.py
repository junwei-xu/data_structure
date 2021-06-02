#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/2 21:25
# description 归并排序

def merge(left_list, right_list):
    """合并，将两个数组合并成有序的大数组，返回一个新数组"""
    # 归并两个有序数组（设置左右指针，比较取小的同时前移小的指针，再比较）
    left, right = 0, 0  # 指针
    result = []  # 结果
    while left < len(left_list) and right < len(right_list):
        if left_list[left] < right_list[right]:
            result.append(left_list[left])
            left += 1
        else:
            result.append(right_list[right])
            right += 1
    # 多余的放到有序数组中
    result += left_list[left:]
    result += right_list[right:]
    return result


def merge_sort(data_list: list):
    """分解再合并"""
    # 元素只有一个时递归结束
    if len(data_list) <= 1:
        return data_list
    # 二分分解
    mid = len(data_list) // 2
    left_list = merge_sort(data_list[:mid])
    right_list = merge_sort(data_list[mid:])

    # 合并
    return merge(left_list, right_list)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    li = merge_sort(li)
    print(li)
