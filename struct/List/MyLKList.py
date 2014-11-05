# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrHero'


class Node(object):
    """
    线性表的存储结构
    和 C 语言中的链式存储结构类似
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LKList(object):
    """
    线性表的具体操作
    """

    def __init__(self):
        """
        相当于初始化线性表, 即创建头结点
        头节点为空节点，占据位置号为0
        创建好的表即为: 头节点[0]->节点[1]->节点[2]->节点[3]->节点[4]
        :return:
        """
        self.L = Node(None)
        self.L.next = None
        self.length = 0

    def is_empty(self):
        """
        判断线新表的长度
        :return:
        """
        return self.length == 0

    def get_length(self):
        """
        获取线新表的长度
        :return:
        """
        return self.length

    def insert(self, i, elem):
        """
        在指定位i处置插入元素elem
        :param i: 指定的位置
        :param elem: 插入的元素elem
        :return:
        """
        j = 0
        p = self.L
        while j < i-1 and p is not None:  # 查找第 i-1 个节点
            j += 1
            p = p.next
        if p is None:   # 未找到逻辑位序为 i-1 的节点
            raise IndexError("Index is out of range!")
        else:   # 找到逻辑位序为 i-1 的节点
            tmp = Node(elem)
            tmp.next = p.next
            p.next = tmp
            self.length += 1

    def delete(self, i):
        """
        删除指定节点的元素
        :param i: 指定节点
        :return: 删除的指定节点元素值
        """
        if self.is_empty():
            raise IndexError("The list is empty!")
        elif 0 < i <= self.length:
            j = 1
            p = self.L
            while j < i and p:
                p = p.next
                j += 1
            delelte_node = p.next
            p.next = delelte_node.next
            self.length -= 1
            return delelte_node.data
        else:
            raise IndexError("Index is out of range!")

    def get_elem(self, i):
        """
        获取某个节点的值
        :param i:
        :return:返回某个节点的值
        """
        if self.is_empty():
            raise IndexError("The list is empty")
        elif 0 < i <= self.length:
            j = 0
            p = self.L
            while j < i and p:
                p = p.next
                j += 1
            print p.data
        else:
            raise IndexError("Index is out of range!")

    def locate_elem(self, elem):
        """
        查找某值的位置
        :param elem:
        :return: 返回第一个值等于elem的位置
        """
        j = 0
        p = self.L
        while p is not None and p.data != elem:
            p = p.next
            j += 1
        if p is Node:
            return -1
        else:
            return j

    def create_dict_list_H(self, list):
        """
        头插法建表
        :param list:
        :return:
        """
        p = self.L
        for i in range(len(list)):
            tmp = Node(list[i])
            tmp.next = p.next
            p.next = tmp
            self.length += 1

    def create_dict_list_E(self, list):
        """
        尾插法建表
        :param list:
        :return:
        """
        p = self.L
        r = p
        for i in range(len(list)):
            tmp = Node(list[i])
            r.next = tmp
            r = tmp
            self.length += 1
        r.next = None

    def show_lklist(self):
        if self.is_empty():
            raise IndexError("It's a empty list!")
        else:
            j = 1
            p = self.L
            while j <= self.length and p:
                p = p.next
                if p is not None:
                    print p.data
                j += 1


if __name__ == '__main__':
    lk = LKList()
    #
    # lk.create_dict_list_E([1, 2, 3, 4])
    # print "-----"
    # lk.get_elem(1)
    # lk.get_elem(2)
    # lk.get_elem(3)
    # lk.get_elem(4)
    # print "-------"
    # lk.show_lklist()
    # lk.insert(3, 5)
    # print "-------"
    # lk.show_lklist()
    # lo = lk.locate_elem(5)
    # print "location is %d" % lo
    # lk.delete(4)
    # print "-------"
    # lk.show_lklist()

