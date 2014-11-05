# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrHero'
"""
串的顺序存储结构有两种: 非紧缩格式, 紧缩格式
非紧缩格式: 每个单元只存一个字符
紧缩格式: 每个单元放多个字符
"""


class SqString(object):

    def __init__(self, size=0):
        self.data = list(None for _ in range(size))
        self.max_size = size
        self.length = 0

    def assign(self, str):
        # 将字符串常量赋值为串s, 即生成一个值等于cstr的串
        for i, item in enumerate(str):
            self.data[i] = item
            self.length += 1

    def show_str(self):
        # 将字符串输出
        if self.length == 0:
            raise ValueError("SqString is empty!")
        for i, item in enumerate(self.data):
            if item is None:
                break
            else:
                print item,
        print ""

    def copy(self, sqrstr):
        # 将该串复制给 sqrstr
        if self.length == 0:
            sqrstr.length = 0
            sqrstr.max_size = self.max_size
            sqrstr.data = list(None for _ in range(self.max_size))
        else:
            sqrstr.length = self.length
            sqrstr.max_size = self.max_size
            sqrstr.data = list(None for _ in range(self.max_size))
            for i, item in enumerate(self.data):
                sqrstr.data[i] = item

    def equal(self, sqstr):
        # 判断串相等: 若两个串s 与 t 相等返回 True, 否则返回 False
        if self.length != sqstr.length:
            return False
        for i in range(self.length):
            if self.data[i] != sqstr.data[i]:
                return False
        return True

    def get_length(self):
        return self.length

    def concat(self, sqstr):
        # 串连接
        result = SqString()
        result.length = self.length + sqstr.length
        result.data = list(None for _ in range(self.max_size + sqstr.max_size))
        # 先将自身复制到result中
        for i in enumerate(self.data):
            result.data[i] = self.data[i]
        # 再将sqstr复制到result中
        for i in enumerate(sqstr.data):
            result.data[self.length + i] = sqstr.data[i]
        return result

    def sub_str(self, i, j):
        # 求字串: 返回串s 中从第 i(1<= i <= StrLength(s)) 个字符开始，由连续
        # j个字符组成的子串
        pass

    def ins_str(self, i, sqstr):
        # 将串 sqstr 插入到 该串




if __name__ == '__main__':
    sqstr = SqString(30)
    ss = "abcdefghijklmnopqlstuvwxyz"
    sqstr.assign(ss)
    sqstr.show_str()
    sqtest = SqString()
    sqstr.copy(sqtest)
    sqtest.show_str()
    a = sqstr.equal(sqtest)
    print a