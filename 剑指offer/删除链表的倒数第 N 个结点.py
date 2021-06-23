#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/23 18:35
# description 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def 字节面试_removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head
        # 删除的是头结点
        cur = head
        if not cur.next:
            return cur.next

        low = fast = head

        # fast先走n步
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            low = low.next
            fast = fast.next
        # low是pre，low.next为cur
        # 删除
        low.next = low.next.next
        return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        # step1: 快指针先走n步
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next

            # step2: 快慢指针同时走，直到fast指针到达尾部节点，此时slow到达倒数第N个节点的前一个节点
        while fast and fast.next:
            slow, fast = slow.next, fast.next

            # step3: 删除节点，并重新连接
        slow.next = slow.next.next
        return dummy.next
