#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/7/20 21:21
# description 输入两个链表，找出它们的第一个公共节点。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 假设公共部分为c，非公共部分一个是a-c 一个是b-c；这样一个加b，一个加a，就能相等相交
        # 指针 A 先遍历完链表 headA ，再开始遍历链表 headB;指针 B 先遍历完链表 headB ，再开始遍历链表 headA;实现上述效果
        A, B = headA, headB
        while A != B:  # 如果不相交，最后的A.next就是null
            A = A.next if A else headB
            B = B.next if B else headA
        return A
