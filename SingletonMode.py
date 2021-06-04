#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/4 10:16
# description
class SingletonMode(object):
    __INSTANCE = None
    __FIRST = True

    def __new__(cls, name):
        if not cls.__INSTANCE:
            cls.__INSTANCE = object.__new__(cls)
        return cls.__INSTANCE

    def __init__(self, name):
        if self.__FIRST:
            self.name = name
            self.__FIRST = False


if __name__ == '__main__':
    a = SingletonMode("小明")
    b = SingletonMode("小红")
    print('单例模式实例化')

    print('两个内存地址:')
    print(id(a))
    print(id(b))

    print('\n实例对象的属性值:')
    print(a.name)
    print(b.name)

    print('\n更改属性值:')
    a.name = '小白'
    print(a.name)
    print(b.name)
