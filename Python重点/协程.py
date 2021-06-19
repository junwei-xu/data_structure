#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/15 18:32
# description
# consumer是一个生成器
def consumer():
    r = ''
    while True:
        # 4.consumer通过yield拿到消息，处理，又通过yield把结果传回
        n = yield r  # yield语句执行完以后，进入暂停，而赋值语句在下一次启动生成器的时候首先被执行
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    # 2.启动生成器
    c.send(None)  # 类似于next(c)，这里返回是空值
    n = 0
    # 5.produce拿到consumer处理的结果，继续生产下一条消息
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        # 3.一旦生产了东西就切换到consumer执行
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    # 6.produce决定不生产了，通过c.close()关闭consumer，整个过程结束
    c.close()


c = consumer()
# 1.把生成器传入produce
produce(c)
