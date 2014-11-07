# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrHero'

import copy


class Node(object):

    def __init__(self, data=None):
        """
        data 传入的是以个list序列，序列的每一位则是要排序的 key
        """
        self.data = data
        self.length = len(data) if data is not None else 0


def show_node(node):
    # 显示node.data 序列
    for index, item in enumerate(node.data):
        print item,
    print ""


def insert_sort(node, n):
    """
    对 node 的 node.data[0, ... ,n-1]进行直接插入排序.
    在 node.data[0...n-1]中, 排序过程的某一中间时刻，node.data被划分成两个子区间
    node.data[0..i-1] 和 node.data[i...n-1], 刚开始时 i=1, 有序区号只有 node.data[0]
    一个记录。前一个子区是已经排好的有序区，后一子序区则是当前为排序的无序区。
    :param node:
    :param n:
    :return:
    """
    tmp = 0
    for i in range(1, n):
        j = i - 1
        tmp = node.data[i]
        while j >= 0 and tmp < node.data[j]:
            node.data[j+1] = node.data[j]
            j -= 1
        node.data[j+1] = tmp
        show_node(node)


def binary_insert_sort(node, n):
    tmp = 0
    for i in range(1, n):
        tmp = node.data[i]
        low = 0
        high = i - 1
        while low <= high:
            mid = (low + high)/2
            if tmp < node.data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        j = i - 1
        while j >= high:
            node.data[j+1] = node.data[j]
            j -= 1
        node.data[high+1] = tmp
        show_node(node)


def bubble_sort(node, n):
    """
    冒泡排序
    通过无序区中相邻记录关键字间的比较和位置的交换,使关键字最小的记录换至较大的记录之上
    """
    for i in range(0, n):
        exchange = 0
        for j in range(n-1, i, -1):
            if node.data[j] < node.data[j-1]:
                node.data[j], node.data[j-1] = node.data[j-1], node.data[j]
                exchange = 1

        show_node(node)
        if exchange == 0:
            return


def quick_sort(node, s, t):
    """
    对node.data[s] 到 node.data[t] 的元素进行快速排序
    快速排序
    :param node:
    :param s:
    :param t:
    """
    i, j = (s, t)
    tmp = 0
    if s < t:
        tmp = node.data[s]
        while i != j:
            while j > i and node.data[j] >= tmp:
                j -= 1
            node.data[i] = node.data[j]
            while i < j and node.data[i] <= tmp:
                i += 1
            node.data[j] = node.data[i]
            show_node(node)
        node.data[i] = tmp
        # show_node(node)
        quick_sort(node, s, i-1)
        quick_sort(node, i+1, t)


def select_sort(node, n):



if __name__ == '__main__':
    ll = [1, 2, 9, 7, 1, 6, 5, -1]
    source = Node(ll)

    # for index, item in enumerate(tar.data):
    #     print i, item

    print "..........源序列........"
    tar1 = copy.deepcopy(source)
    show_node(tar1)
    print "..........直接插入排序........"
    insert_sort(tar1, tar1.length)
    print "..........二分插入排序........"
    tar2 = copy.deepcopy(source)
    binary_insert_sort(tar2, tar2.length)
    print "..........冒泡排序........"
    tar3 = copy.deepcopy(source)
    bubble_sort(tar3, tar3.length)
    print "..........快速排序........"
    tar4 = copy.deepcopy(source)
    show_node(tar4)
    quick_sort(tar4, 0, tar4.length-1)
