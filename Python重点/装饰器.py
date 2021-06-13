#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/13 21:43
# description

# 装饰器
import functools
import time


def cal_time(func):
    @functools.wraps(func)  # 保留函数原有信息
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)

        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()

        print('time cost:', end_time - start_time)

    return wrapper


@cal_time
def run():
    res = 0
    for i in range(1000):
        for j in range(10000):
            res += 1
            res -= 1
    return res


if __name__ == '__main__':
    run()
