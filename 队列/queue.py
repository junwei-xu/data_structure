#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/29 22:59
# description 队列（顺序表实现） FIFO
class Queue(object):
    def __init__(self, size=5):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [None] * size

    def is_full(self):
        """是否队列满"""
        return self.rear - self.front + 1 == self.size

    def is_empty(self):
        """是否队列空"""
        return self.rear - self.front == 0

    def enqueue(self, item):
        """入队列"""
        if self.is_full():
            raise Exception('queue is full')
        else:
            self.queue[self.rear + 1] = item
            self.rear += 1

    def dequeue(self):
        """出队列"""
        if self.is_empty():
            raise Exception('queue is empty')
        else:
            self.queue[self.front + 1] = None
            self.front += 1


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    print('after enqueue:', queue.queue)

    queue.dequeue()
    print('after dequeue:', queue.queue)
