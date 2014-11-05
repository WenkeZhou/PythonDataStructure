# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "MrHero"


class Node():
    #单个节点
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList():

    def __init__(self):
        self.L = Node(None) #头结点
        self.L.next = None
        self.__r = self.L
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def get_length(self):
        return self.length

    def create(self, elem):
        p = Node(elem)
        self.__r.next = p
        self.__r = self.__r.next
        self.length += 1

    def get_elem(self, i):
        if self.is_empty():
            raise IndexError('LinkList is empty.')
        elif 0< i <= self.length:
            j = 1
            p = self.L.next
            while p and j < i:
                j += 1
                p = p.next
            elem = p.data
            return elem
        else:
            raise IndexError('Index is out of range.')

    def insert(self, i, elem):
        if self.is_empty() and i == 1:
            self.L.next = Node(elem)
            self.length += 1
        else:
            if 0 < i <= self.length:
                j = 1
                p = self.L
                while p and j < i:
                    p = p.next
                    j += 1
                n = Node(elem)
                n.next = p.next
                p.next = n
                self.length += 1
            else:
                raise IndexError('out of index')

    def delete(self, i):
        if self.is_empty():
            raise IndexError('out of index')
        else:
            if 0 < i <= self.length:
                j = 1
                p = self.L
                while p and j < i:
                    p = p.next
                    j += 1
                delnode = p.next
                p.next = delnode.next
                self.length -= 1
                return delnode.data
            else:
                raise IndexError('out of index')

if __name__ == '__main__':
    l = LinkList()