# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrHero'

#顺序表 Sequence List


class SqList():

    def __init__(self, size):
        #方法一：列表推导式
        # self.data = [None for i in range(size)]
        #方法二：生成器表达式 generator
        #两者区别： http://blog.jobbole.com/61171/
        self.data = list(None for _ in range(size)) #保存的数据元素
        self.maxsize = size
        self.length = 0

    def is_empty(self):
        # and or 用法
        # empty = self.length == 0 and True or False
        return self.length == 0

    def is_full(self):
        return self.maxsize == self.length

    def get_length(self):
        return self.length

    def create(self, elem):
        for i, item in enumerate(self.data):
            if self.length < self.maxsize:
                if item is None:
                    self.data[i] = elem
                    self.length += 1
                    break
            else:
                raise IndexError('SqList is full')

    def get_elem(self, i):
        if self.is_empty():
            raise IndexError('SqList is full')
        elif self.length < i or 0 > i:
            raise IndexError('SqList is full')
        else:
            return self.data[i-1]

    def insert(self, i, elem):
        if not self.is_full():
            if 0 < i <= self.length:
                for index in range(self.length - 1, i-2, -1):
                    self.data[index+1] = self.data[index]
                self.data[i-1] = elem
                self.length += 1
        else:
            raise IndexError('SqList is full.')

    def delete(self, i):
        if self.is_empty():
            raise IndexError('SqList is empty.')
        elif 0 < i <= self.length:
            deelem = self.get_elem(i)
            for index in range(i, self.length):
                if index != 0:
                    self.data[index - 1] = self.data[index]
            self.data[self.length - 1] = None
            self.length -= 1
            return deelem
        else:
            raise IndexError('Index is out of range.')

if __name__ == '__main__':
    s = SqList(5)
    for i in range(0, 3):
        s.create(i)
    print(s.data)
