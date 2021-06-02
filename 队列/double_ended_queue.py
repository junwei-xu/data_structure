#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/30 10:20
# description 双端队列（顺序表实现） 任意一端出入队
class Deque(object):
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

    def enqueue_front(self, item):
        """从队头，入队列"""
        if self.is_full():
            raise Exception('queue is full')
        elif self.front == -1:
            raise Exception('front is full')
        else:
            self.queue[self.front] = item
            self.front -= 1

    def enqueue_rear(self, item):
        """从队尾，入队列"""
        if self.is_full():
            raise Exception('queue is full')
        else:
            self.queue[self.rear + 1] = item
            self.rear += 1

    def dequeue_front(self):
        """从队头，出队列"""
        if self.is_empty():
            raise Exception('queue is empty')
        else:
            self.queue[self.front + 1] = None
            self.front += 1

    def dequeue_rear(self):
        """从队尾，出队列"""
        if self.is_empty():
            raise Exception('queue is empty')
        elif self.rear == self.size - 1:
            raise Exception('rear is full')
        else:
            self.queue[self.rear] = None
            self.rear -= 1


if __name__ == "__main__":
    deque = Deque()
    deque.enqueue_rear('a')
    deque.enqueue_rear('b')
    deque.enqueue_rear('c')
    print('after enqueue_rear:', deque.queue)

    deque.dequeue_front()
    print('after dequeue_front:', deque.queue)

    deque.enqueue_front('d')
    print('after enqueue_front:', deque.queue)

    deque.dequeue_rear()
    print('after dequeue_rear:', deque.queue)
