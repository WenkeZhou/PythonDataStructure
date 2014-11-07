# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "MrHero"

"""
基本思路:
从目标串 s="s0 s1 ... s(n-1)"的第一个字符开始 和
模式串 t="t0 t1 .. t(m-1)" 的第一个字符比较，
若相等，则逐个比较后续字符；否则从目标串 s 的第二个字符开始从新与模式串t的第一个字符进行比较。
以此类推。
"""

from SqString import SqString


def brute_force(source, tar):
    """
    采用顺序存储的串 SqString
    类型:
        def __init__(self, size=0):
            self.data = list(None for _ in range(size))
            self.max_size = size
            self.length = 0
    sorce: 为要目标串
    tar: 为模式串
    """
    i = j = 0
    while i < source.length and j < tar.length:
        if source.data[i] == tar.data[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j >= tar.length:
        return i - tar.length # 返回匹配的第一个字符的下标
    else:
        return -1


if __name__ == '__main__':
    source_str = "abcdefghijk"
    tar_str = "cdefg"
    source = SqString(30)
    source.assign(source_str)
    tar = SqString(30)
    tar.assign(tar_str)
    print brute_force(source, tar)





