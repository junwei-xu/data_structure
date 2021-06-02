#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/29 16:39
# description 双链表
class Node(object):
    """定义双链表的结点"""

    def __init__(self, item):
        self.item = item  # 数据域
        self.next = None  # 指针域 next
        self.prev = None  # 指针域 prev


class DoubleLinkedList(object):
    def __init__(self):
        # 头指针
        self.__head = None

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head  # 初始指向头结点
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next  # 后一个结点
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next
        print('\n')

    def add(self, item):
        """头插法"""
        # 新结点
        new_node = Node(item)
        if self.is_empty():
            # 若为空链表，则直接将头指针指向新结点
            self.__head = new_node
        else:
            # 新结点的next指向head的头指针
            new_node.next = self.__head
            # head结点的prev指向新结点
            self.__head.prev = new_node
            # 将头指针指向新结点
            self.__head = new_node

    def append(self, item):
        """尾插法"""
        # 新结点
        new_node = Node(item)
        if self.is_empty():
            # 若为空链表，则直接将头指针指向新结点
            self.__head = new_node
        else:
            # 移动到尾部
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            # 尾结点的next指向新结点
            cur.next = new_node
            # 新结点的prev指向尾结点
            new_node.prev = cur

    def insert(self, pos, item):
        """指定位置插入"""
        # 若指定位置为第一个元素之前，则头插法插入
        if pos < 0:
            self.add(item)
        # 若指定位置超过链表尾部，则尾插法插入
        elif pos > self.length() - 1:
            self.append(item)
        else:
            new_node = Node(item)
            cur = self.__head
            count = 0
            # 找到指定位置的前一个位置
            while count < pos - 1:
                count += 1
                cur = cur.next
            # 将新结点的prev指向前一个位置的结点
            new_node.prev = cur
            # 将新结点的next指向pos位置的结点（即前一个结点的next）
            new_node.next = cur.next
            # 将pos位置（即前一个结点的next）的prev指向新结点
            cur.next.prev = new_node
            # 将pos结点（即前一个结点的next）的next指向新结点
            cur.next = new_node

    def remove(self, item):
        # 删除指定位置结点
        cur = self.__head

        while cur is not None:
            # 如果找到了指定的元素
            if cur.item == item:
                # 如果是头结点
                if cur == self.__head:
                    # 头指针指向下一个结点
                    self.__head = cur.next
                    # 下一个结点的prev为空，即此时下一个结点为头结点
                    cur.next.prev = None
                else:
                    # 前一个结点next指向后一个结点
                    cur.prev.next = cur.next
                    # 后一个结点的prev指向前一个结点
                    cur.next.prev = cur.prev
                break
            else:
                # 找下一个元素
                cur = cur.next

    def search(self, item):
        """查找指定元素是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    dl = DoubleLinkedList()

    print("头插法插入：")
    dl.add(1)
    dl.add(2)
    dl.travel()

    print("尾插法插入：")
    dl.append(3)
    dl.append(4)
    dl.travel()

    print("指定位置插入：")
    dl.insert(2, 5)
    dl.travel()

    print("删除指定结点：")
    dl.remove(3)
    dl.travel()

    print('查找指定结点是否存在：')
    print(dl.search(3))
    print(dl.search(4))
