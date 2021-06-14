#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/6 10:06
# description
# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 解法一：递归实现
    def reversePrint(self, head: ListNode) -> list[int]:
        return self.reversePrint(head.next) + [head.val] if head else []

    # 解法二：利用栈的FILO特性
    def reversePrint_using_stack(self, head: ListNode) -> list[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
