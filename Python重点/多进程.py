#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/19 22:44
# description

from multiprocessing import Pool, Queue, Pipe
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))  # 进程号
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # 进程池
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()  # 调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()  # 调用join()方法会等待所有子进程执行完毕
    print('All subprocesses done.')
