#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/5/29 21:32
# description 单项循环链表

class Node(object):
    """定义单链表的结点"""

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCycleLinkedList(object):
    def __init__(self):
        """头指针"""
        self.__head = None

    def is_empty(self):
        """判断是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head  # 初始指向头结点
        count = 0
        while cur.next != self.__head:
            count += 1
            cur = cur.next  # 后一个结点
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        print(cur.item, end=' ')
        while cur.next != self.__head:
            cur = cur.next
            print(cur.item, end=' ')
        print('\n')

    def add(self, item):
        """头插法"""
        # 新结点
        new_node = Node(item)
        if self.is_empty():
            # 若为空链表，则直接将头指针指向新结点，新结点的next指向头结点
            self.__head = new_node
            new_node.next = self.__head
        else:
            # 新结点的next为原先的头结点
            new_node.next = self.__head

            # 尾结点的next指向新结点
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            cur.next = new_node

            # 头指针指向新结点
            self.__head = new_node

    def append(self, item):
        """尾插法"""
        new_node = Node(item)
        if self.is_empty():
            # 若为空链表，则直接将头指针指向新结点，新结点的next指向头结点
            self.__head = new_node
            new_node.next = self.__head
        else:
            # 找到尾结点
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 将尾结点的next指向新结点
            cur.next = new_node
            # 将新结点的next指向头结点
            new_node.next = self.__head

    def insert(self, pos, item):
        """指定位置添加元素"""
        # 若指定位置为第一个元素之前，则头插法插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则尾插法插入
        elif pos > self.length() - 1:
            self.append(item)
        else:
            new_node = Node(item)
            count = 0
            # 找到指定位置的前一个结点
            pre = self.__head
            while count < pos - 1:
                count += 1
                pre = pre.next
            # 新结点的next指向原本结点（即前一结点的next）
            new_node.next = pre.next
            # 前一结点的next指向新结点
            pre.next = new_node

    def remove(self, item):
        """删除指定结点"""
        cur = self.__head
        pre = None

        while cur.next != self.__head:
            # 如果找到了指定元素
            if cur.item == item:
                # 若为头结点
                if cur == self.__head:
                    # 找尾结点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    # 将头指针指向头结点的下一个结点
                    self.__head = cur.next
                    # 尾结点的next指向头结点
                    rear.next = self.__head
                else:
                    # 中间位置结点
                    # 将前一个结点的next指向后一个结点（即当前结点的next）
                    pre.next = cur.next
                break
            else:
                # 后移寻找
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找指定结点是否存在"""
        cur = self.__head
        if cur.item == item:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return False


if __name__ == '__main__':
    sl = SingleCycleLinkedList()

    print("头插法插入：")
    sl.add(1)
    sl.add(2)
    sl.travel()

    print("尾插法插入：")
    sl.append(3)
    sl.append(4)
    sl.travel()

    print("指定位置插入：")
    sl.insert(2, 5)
    sl.travel()

    print("删除指定结点：")
    sl.remove(3)
    sl.travel()

    print('查找指定结点是否存在：')
    print(sl.search(3))
    print(sl.search(4))
