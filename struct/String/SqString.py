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
        # 求字串: 返回串s 中从第 i(1<= i <= self.length) 个字符开始，由连续
        # j个字符组成的子串
        # 返回新串
        if i <= 0 or i > self.length or i + j - 1 > self.length:
            raise IndexError("Index error!")
        result = SqString(j)
        for k, item in enumerate(self.data[i-1:i+j-1]):
            result.data[k] = item
            result.length += 1
        return result

    def ins_str(self, i, sqstr):
        # 将串 sqstr 插入到 该串的第i 个字符中，即将 sqstr 的第一个字符作为s1的第i个字符，
        # 并返回返回产生的新串
        if i <= 0 or i > self.length:
            raise IndexError("Index is out of range!")
        result = SqString(self.max_size + sqstr.max_size)
        #将 self.data[0:i-2] 复制到result中
        for k, item in enumerate(self.data[0:i-1]):
            result.data[k] = item
            result.length += 1
        #将 sqstr 复制到result中
        # len2 = result.length
        for k, item2 in enumerate(sqstr.data):
            if item2 is not None:
                result.data[i - 1 + k] = item2
                result.length += 1
            else:
                break
        #将 self.data[i-1:] 复制到result中
        # len3 = result.length
        for k, item3 in enumerate(self.data[i-1:]):
            if item3 is not None:
                result.data[i - 1 + sqstr.length + k] = item3
                result.length += 1
            else:
                break
        return result

    def del_str(self, i, j):
        # 从串s 中删除第 i (1<= i <= self.length) 个字符开始，长度为j的字串
        # 并返回产生的新串
        # 参数不正确时返回一个空串
        if i <= 0 or i > self.length or i + j - 1 > self.length:
            raise IndexError("Index is out of range")
        result = SqString(self.length - j)
        for k, item in enumerate(self.data[0:i]):
            result.data[k] = item
            result.length += 1
        for k, item in enumerate(self.data[i + j - 1:]):
            if item is not None:
                result.data[i - 1 + k] = item
                result.length += 1
            else:
                break
        return result

    def rep_str(self, i, j, sqstr):
        # 在串self中，将第i(1<= i <= self.length)个字符开始的j个字符构成的子串用串t替换，
        # 并返回产生的新串。
        # 参数不正确是返回一个空串。
        if i <= 0 or i > self.length or i + j - 1 > self.length:
            raise IndexError("Index is out of range")
        result = SqString(self.length - j + sqstr.length)
        for k, item in enumerate(self.data[0:i]):
            result.data[k] = item
            result.length += 1
        for k, item in enumerate(sqstr.data):
            if item is not None:
                result.data[i - 1 + k] = item
                result.length += 1
        for k, item in enumerate(self.data[i + j - 1:]):
            if item is not None:
                result.data[i - 1 + sqstr.length + k] = item
                result.length += 1
        return result


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
    result = sqstr.sub_str(3, 5)
    result.show_str()

    sss = "123"
    test1 = SqString(5)
    test1.assign(sss)
    result2 = sqstr.ins_str(3, test1)
    result2.show_str()

    result3 = result2.del_str(5, 6)
    result3.show_str()

    result4 = result3.rep_str(5, 4, test1)
    result4.show_str()