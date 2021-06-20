#!/usr/bin/python3
# _*_coding=utf-8 _*_
# @author junwei
# @date 2021/6/20 10:31
# description
# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
# 示例1：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 初始化一个辅助节点 dum作为合并链表的伪头节点，将各节点添加至 dum之后
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next  # 更新cur位置
        cur.next = l1 if l1 else l2  # 不要忘记最后剩下的
        return dum.next
