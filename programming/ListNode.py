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

    def __str__(self):
        return 'The ListNode begin with %s' %self.val

    def _append(self, head, val, location=-1):
        """
        向链表中添加元素
        :param head: 链表头
        :param val: 添加的值
        :param location: 插入的位置，默认为最后 (暂时未实现使用负数进行遍历）
        :return: 链表
        """
        loca = 1
        temp = ListNode(val)
        p = head

        if location == -1:
            while p.next:
                p = p.next
            p.next = temp

        elif location < -1:
            raise IndexError('%s Out of Range' % head)

        else:
            while p.next and loca < location:
                loca = loca + 1
                p = p.next

            temp.next = p.next
            p.next = temp




def main():
    a = ListNode(5)
    h = a
    a._append(a, 100)
    a._append(a, 200)
    a._append(a, 300)

    while h:
        print(h.val)
        h = h.next

    a._append(a, -100, 2)
    print("*"*100)
    h = a
    while h:
        print(h.val)
        h = h.next

if __name__ == "__main__":
    main()

