# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrHero'


class Node(object):
    # 节点
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LkQueue():

    def __init__(self):
        self.front = Node()
        self.rear = Node()
        self.length = 0

    def get_length(self):
        return self.length

    def is_empty(self):
        empty = self.length == 0 and True or False
        return empty

    def enQueue(self, elem):
        # 入队
        tmp = Node(elem)
        if self.is_empty():
            self.front = tmp
            self.rear = tmp
        else:
            self.rear.next = tmp
            self.rear = tmp
        self.length += 1

    def deQueue(self):
        # 出队
        if self.is_empty():
            raise ValueError("LKQueue is empty!")
        else:
            del_elem = self.front.data
            self.front = self.front.next
            self.length -= 1
            return del_elem

    def showQueue(self):
        # 从对首 出队
        if self.is_empty():
            raise ValueError("LKQueue is empty!")

        j = self.length
        tmp = self.front
        while j > 0:
            print tmp.data,
            tmp = tmp.next
            j -= 1
        print ''


if __name__ == '__main__':
    lkq = LkQueue()
    for i in range(5):
        lkq.enQueue(i)
    lkq.showQueue()
    print ";;;;;;;;;"
    lkq.deQueue()
    lkq.showQueue()
