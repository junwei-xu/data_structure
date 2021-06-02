#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/30 13:51
# description 循环队列
class CirQueue(object):
    def __init__(self, size=5):
        self.size = size
        self.front = 0
        self.rear = 0
        self.queue = [None] * size

    def is_full(self):
        """是否队列满"""
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        """是否队列空"""
        return self.rear - self.front == 0

    def enqueue(self, item):
        """入队列"""
        if self.is_full():
            raise Exception('queue is full')
        else:
            self.queue[self.rear + 1] = item
            self.rear = (self.rear + 1) % self.size

    def dequeue(self):
        """出队列"""
        if self.is_empty():
            raise Exception('queue is empty')
        else:
            self.queue[self.front + 1] = None
            self.front = (self.front + 1) % self.size

    def get_length(self):
        """队列长度"""
        return (self.rear - self.front + self.size) % self.size


if __name__ == "__main__":
    queue = CirQueue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    queue.enqueue('d')
    print('after enqueue:', queue.queue)

    queue.dequeue()
    print('after dequeue:', queue.queue)
