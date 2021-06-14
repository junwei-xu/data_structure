#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/5 23:01
# description
# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
class Solution:

    # 没仔细看题 超时
    def binary_search(self, array, item):
        if len(array) == 0:
            return False
        else:
            mid = len(array) // 2
            if array[mid] == item:
                return True
            else:
                if item < array[mid]:
                    return self.binary_search(array[:mid], item)
                else:
                    return self.binary_search(array[mid + 1:], item)

    def blpj(self, matrix: list[list[int]], target: int) -> bool:
        row, col = 0, 0
        matrix_col = [i[col] for i in matrix]
        while row <= len(matrix) and col <= len(matrix_col):
            if matrix[row][col] <= target <= matrix[row][-1]:
                res_row = self.binary_search(matrix[row], target)
                if not res_row:
                    if matrix_col[0] <= target <= matrix_col[-1]:
                        res_col = self.binary_search(matrix_col, target)
                        if not res_col:
                            col += 1
                            row += 1
                        else:
                            return True
                else:
                    return True

    # 解法：线性查找
    # 如果从左上角开始找，那么如果当前数比目标值小的话，向下走或者向右走都可以让数变大，方向就不能确定
    # 所以应该找从两个方向走一个是变大的一个变小的位置作为起始位置，比如右上角和左下角
    def findNumberIn2DArray(self, matrix: list[list[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        su_row = len(matrix)
        su_col = len(matrix[0])
        row, col = 0, su_col - 1  # 从右上角开始
        while row < su_row and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:  # 比他小就往下找
                row += 1
            else:  # 比他大就往左找
                col -= 1
        return False


if __name__ == '__main__':
    if __name__ == '__main__':
        Solution().findNumberIn2DArray([
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ], 5)
