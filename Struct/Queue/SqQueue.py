# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrHero'


class SqQueue():

    def __init__(self, size):
        self.data = list(None for _ in range(size + 1))
        self.maxsize = size + 1
        self.front = 0
        self.rear = 0
        self.length = 0

    def get_length(self):
        return self.length

    def is_full(self):
        full = (self.rear + 1) % self.maxsize == self.front and True or False
        return full

    def is_empty(self):
        empty = self.rear == self.front and True or False
        return empty

    def enQueue(self, elem):
        #进队列,从队尾插入
        if self.is_full():
            raise IndexError("Queue is full!")
        else:
            self.data[self.rear] = elem
            self.rear = (self.rear + 1) % self.maxsize
            self.length += 1

    def deQueue(self):
        #出队列，从队首删除
        if self.is_empty():
            raise ValueError("SqQueue is empty!")
        else:
            del_elem = self.data[self.front]
            self.data[self.front] = None
            self.front = (self.front + 1) % self.maxsize
            self.length -= 1
            return del_elem

    def show_queue(self):
        #显示队列元素， 从队首开始显示
        if self.is_empty():
            raise ValueError("SqQueue is empty!")
        else:
            j = self.front
            while j != self.rear:
                print self.data[j],
                j = (j + 1) % self.maxsize
            print ''

if __name__ == '__main__':
    sqq = SqQueue(5)
    for i in range(5):
        sqq.enQueue(i)
    sqq.show_queue()
    print ".............."
    sqq.deQueue()
    sqq.show_queue()