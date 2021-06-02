#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/30 20:47
# description 快速排序

# def quick_sort(data_list: list):
#     """伪快排,效率低,直接按照定义实现"""
#     size = len(data_list)
#     # 递归出口,空数组或只有一个元素的数组都是有序的
#     if data_list is None or size < 2:
#         print(data_list)
#         return data_list
#     # 基准值
#     pivot_index = 0
#     pivot = data_list[pivot_index]
#     # 将数组分成两个子数组：小于基准值的元素和大于基准值的元素
#     less_part = [data_list[i] for i in range(size) if data_list[i] <= pivot and pivot_index != i]
#     more_part = [data_list[i] for i in range(size) if data_list[i] > pivot and pivot_index != i]
#     # 继续递归
#     return quick_sort(less_part) + [pivot] + quick_sort(more_part)

def partition(data_list: list, left, right):  # [left,right]
    """设置首位两个个指针 left, right，两个指针不断向中间收拢。
    如果遇到 left 位置的元素大于 pivot 并且 right 指向的元素小于 pivot，就交换这俩元素;
    当 left > right 的时候退出，这样实现了一次遍历就完成了 partition"""
    pivot = data_list[left]  # 第一个为基准值

    while left < right:
        # 从右往左找,如果right指向的元素比pivot大,那right指针向中间收拢;否则和left交换
        while left < right and data_list[right] >= pivot:
            right -= 1
        data_list[left] = data_list[right]  # 直接覆盖,因为原本的left元素已经保存在pivot中了

        # 从左往右找,如果left指向的元素比pivot小,那left指针向中间收拢;否则和right交换
        while left < right and data_list[left] < pivot:
            left += 1
        data_list[right] = data_list[left]

    data_list[left] = pivot
    return left  # 新的pivot位置


def quick_sort(data_list: list, left, right):  # [left,right]
    # 当left = right的时候递归结束
    if left < right:
        pivot = partition(data_list, left, right)
        quick_sort(data_list, left, pivot - 1)
        quick_sort(data_list, pivot + 1, right)
    return data_list


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(quick_sort(li, 0, len(li) - 1))
