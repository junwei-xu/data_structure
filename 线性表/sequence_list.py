#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/29 10:57
# description 顺序表实现
class SeqList(object):
    def __init__(self, max=50):
        """初始化顺序表"""
        self.max = max  # 最大长度
        self.size = 0  # 当前长度
        self.data = [None] * self.max  # 初始化列表

    def is_empty(self):
        """判断顺序表是否为空"""
        return self.size == 0

    def is_full(self):
        """判断顺序表是否为满"""
        return self.size == self.max

    def __getitem__(self, index):  # 当按照键取值时，可以直接返回__getitem__方法执行的结果
        """获取顺序表中某一位置的值"""
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.max:
            return self.data[index]
        else:
            raise IndexError

    def __setitem__(self, index, value):
        """修改顺序表中某一位置的值"""
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.max:
            self.data[index] = value
        else:
            raise IndexError

    def append_last(self, value):
        """在表尾插入一个元素"""
        if self.is_full():
            raise Exception("list is full")
        else:
            self.data[self.size] = value
            self.size += 1

    def insert(self, index, value):
        """在任意位置插入一个元素"""
        if not isinstance(index, int):
            raise TypeError
        if not 0 <= index < self.max:
            raise IndexError
        if self.is_full():
            raise Exception('list is full')
        # index后的所有元素后移一个位置
        for i in range(self.size, index - 1, -1):
            self.data[i + 1] = self.data[i]
        # 插入，+1
        self.data[index] = value
        self.size += 1

    def remove(self, index):
        """删除表中某一位置的值"""
        if not isinstance(index, int):
            raise TypeError
        if not 0 <= index < self.max:
            raise IndexError
        # index后的所有元素前移覆盖
        for i in range(index - 1, self.size):
            self.data[i] = self.data[i + 1]
        self.size -= 1

    def destroy(self):
        """销毁顺序表"""
        self.__init__()

    def print_list(self):
        """打印"""
        for i in range(self.size):
            print(self.data[i], end=' ')


if __name__ == '__main__':
    seqlist = SeqList()
    print('\n初始顺序表：')
    seqlist.print_list()

    print('\n表尾添加元素后：')
    for i in range(10):
        seqlist.append_last(i + 1)
    seqlist.print_list()

    print('\n在第5位插入元素后：')
    seqlist.insert(4, 'insert')
    seqlist.print_list()

    print('\n删除第5位元素后：')
    seqlist.remove(5)
    seqlist.print_list()

    # print(seqlist[0])  # 即print(seqlist.__getitem__(0))
