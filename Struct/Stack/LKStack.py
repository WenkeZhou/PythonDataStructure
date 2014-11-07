# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrHero'


class Node(object):
    # 节点
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LKStack(object):

    def __init__(self):
        self.top = Node(None)
        self.count = 0

    def get_length(self):
        return self.count

    def get_top(self):
        # 返回栈顶元素
        return self.top.data

    def is_empty(self):
        return self.count == 0

    def push(self, elem):
        # 进栈
        tmp = Node(elem)
        if self.is_empty():
            self.top = tmp
        else:
            tmp.next = self.top
            self.top = tmp
        self.count += 1

    def pop(self):
        # 出栈
        if self.is_empty():
            raise IndexError("Stack is empty!")
        else:
            self.count -= 1
            elem = self.top.data
            self.top = self.top.next
            return elem

    def show_stack(self):
        # 从栈顶开始显示各节点值
        if self.is_empty():
            raise IndexError("Stack is empty!")
        else:
            j = self.count
            tmp = self.top
            while j > 0 and tmp:
                print tmp.data
                tmp = tmp.next
                j -= 1

if __name__ == '__main__':
    lks = LKStack()
    for i in range(1, 5):
        lks.push(i)
    lks.show_stack()
    lks.pop()
    lks.show_stack()
