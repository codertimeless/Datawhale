#!/usr/bin/env python
# -*- coding:utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        """
        初始化链表
        :param x:val
        """
        self.val = x
        self.next = None

    def __len__(self, head):
        if not head:
            return 0

        l = 0
        while head:
            l = l + 1
            head = head.next

        return l

    def append(self, head, val, *location):
        while head.next:
            head = head.next

        temp = ListNode(val)
        head.next =temp


a = ListNode(5)


