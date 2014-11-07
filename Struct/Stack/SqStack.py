# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrHero'


class SqStack(object):
    """
    栈的线性结构
    """

    def __init__(self, size):
        self.data = list(None for _ in range(size))
        self.max_size = size
        self.top = -1

    def get_length(self):
        # 返回栈的长度
        return self.top + 1

    def push(self, elem):
        # 进栈
        if self.top + 1 == self.max_size:
            raise IndexError("Stack is full")
        else:
            self.top += 1
            self.data[self.top] = elem

    def pop(self):
        # 出栈
        if self.top == -1:
            raise IndexError("Stack is empty")
        else:
            self.top -= 1
            return self.data[self.top + 1]

    def get_top(self):
        # 取栈顶元素
        if self.top == -1:
            raise IndexError("Stack is empty")
        else:
            return self.data[self.top]

    def show_stack(self):
        # 从栈顶向下开始显示栈里面的元素
        j = self.top
        while j >= 0:
            print self.data[j]
            j -= 1

    def is_empty_stack(self):
        return self.top == -1

if __name__ == '__main__':
    sqs = SqStack(5)
    sqs.push(1)
    sqs.push(2)
    sqs.push(3)
    sqs.show_stack()

