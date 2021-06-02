#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/29 22:31
# description 栈（顺序表实现） FILO
class Stack(object):
    def __init__(self, size=5):
        self.size = size
        self.stack = [None] * size
        self.top = -1

    def is_empty(self):
        """是否栈空"""
        return self.top == -1

    def is_full(self):
        """是否栈满"""
        return self.size == self.top + 1

    def push(self, item):
        """添加"""
        if self.is_full():
            raise Exception('stack is full')
        else:
            self.stack[self.top + 1] = item
            self.top += 1

    def pop(self):
        """弹出"""
        if self.is_empty():
            raise Exception('stack is empty')
        else:
            self.stack[self.top] = None
            self.top -= 1

    def peek(self):
        """返回栈顶元素"""
        return self.stack[self.top]


if __name__ == "__main__":
    stack = Stack()
    stack.push("a")
    stack.push("b")
    stack.push("c")
    print("after push:", stack.stack)
    print('peek:', stack.peek())
    stack.pop()
    print("after pop:", stack.stack)
