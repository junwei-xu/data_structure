#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/6 19:48
# description 用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

class CQueue:

    def __init__(self):
        self.stack_a, self.stack_b = [], []

    # 解法一：直观理解 反复倒腾
    def fir_appendTail(self, value: int) -> list:
        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())
        self.stack_a.append(value)
        while self.stack_b:
            self.stack_a.append(self.stack_b.pop())
        return self.stack_a

    def fir_deleteHead(self) -> int:
        if not self.stack_a:
            return -1
        return self.stack_a.pop()

    # 解法二：优化，更高效利用两个栈
    def appendTail(self, value: int) -> None:
        self.stack_a.append(value)

    def deleteHead(self) -> int:
        if self.stack_b:  # 如果栈b还有倒序的元素就直接弹出
            return self.stack_b.pop()
        if not self.stack_a:  # 如果栈b和栈a都没元素，-1
            return -1
        while self.stack_a:  # 栈a倒序放到栈b
            self.stack_b.append(self.stack_a.pop())

        return self.stack_b.pop()  # 正常弹出一个
