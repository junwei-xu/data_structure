#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/14 11:38
# description
# 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# Definition for singly-linked list.
from functools import reduce


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 解法一：迭代
    def dd_reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while cur:
            nex = cur.next  # 当前结点的下一个结点
            cur.next = pre  # 更新当前结点的下一个结点为pre
            pre = cur  # 更新pre结点
            cur = nex  # 更新cur结点
        return pre

    # 解法二：递归
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)  # new_head = 5,head = 4
        head.next.next = head  # 5指向4
        head.next = None
        return new_head

    # 解法2.1：递归，基本原理同上；但用了双指针便于理解
    def reverseList3(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, cur = head, head.next
        new_head = self.reverseList(cur)
        cur.next = pre
        pre.next = None
        return new_head
