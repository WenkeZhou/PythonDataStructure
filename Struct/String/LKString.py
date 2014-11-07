# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrHero'


class Node(object):
    # 节点
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LKString(object):
    """
    串的链式存储结构
    """
    def __init__(self):
        self.L = Node()
        self.next = None
        self.length = 0

    def assign(self, cstr):
        # 将字符串cstr 赋值给串s, 即生成一个值等于cstr的串self, 采用尾插法
        p = self.L
        for i, item in enumerate(cstr):
            tmp = Node(item)
            p.next = tmp
            p = tmp
            self.length += 1
        p.next = None

    def copy(self, lkstr):
        # 将串 lkstr 的值复制给self
        r = self.L
        p = lkstr.L.next
        j = lkstr.length
        while j >= 0 and p:
            tmp = Node(p.data)
            r.next = tmp
            r = tmp
            p = p.next
            self.length += 1
        r.next = None

    def show_str(self):
        # 输出字符串，将字符串重头部到尾部显示出来
        p = self.L
        j = self.length
        while j >= 0 and p.next:
            p = p.next
            print p.data,
            j -= 1
        print ""

    def equal(self, lkstr):
        # 判断两个串是否相等
        if self.length != lkstr.length:
            return False
        j = self.length
        r = self.L.next
        p = lkstr.L.next
        while j > 0:
            if r.data != p.data:
                return False
            else:
                j -= 1
                r = r.next
                p = p.next
        return True

    def get_length(self):
        return self.length

    def contact(self, lkstr):
        # 返回由两个串s 和 t链接在一起形成的新串，采用尾插法
        result = LKString()
        r = result.L
        # 将self插入到result中
        len1 = self.length
        p = self.L.next
        while len1 > 0 and p:
            tmp = Node(p.data)
            r.next = tmp
            r = tmp
            len1 -= 1
            result.length += 1
            p = p.next
        # 将lkstr插入到result中
        q = lkstr.L.next
        len2 = lkstr.length
        while len2 > 0 and q:
            tmp = Node(q.data)
            r.next = tmp
            r = tmp
            len2 -= 1
            result.length += 1
            q = q.next
        r.next = None
        return result

    def substr(self, i, j):
        # 串self, 将第 i 个字符开始的 j个字符串生成以个子串
        result = LKString()
        if i < 0 or i > self.length or i + j -1 > self.length:
            raise IndexError("Index is out of range.")
        current = self.L
        r = result.L
        for _ in range(i-1):
            current = current.next
        for _ in range(j):
            current = current.next
            tmp = Node(current.data)
            r.next = tmp
            r = tmp
            result.length += 1
        return result

    def insstr(self, i, lkstr):
        # 将串lkstr 插入到串self的第 i 个字符位置
        if i <= 0 or i > self.length:
            raise IndexError("Index is out!")
        result = LKString()
        r = result.L
        current = self.L.next
        for _ in range(i-1):
            tmp = Node(current.data)
            r.next = tmp
            r = tmp
            result.length += 1
            current = current.next

        tail = current

        lkstr_cur = lkstr.L.next
        lkstr_len = lkstr.length
        while lkstr_len > 0 and lkstr_cur:
            tmp = Node(lkstr_cur.data)
            r.next = tmp
            r = tmp
            result.length += 1
            lkstr_cur = lkstr_cur.next
        while tail:
            tmp = Node(tail.data)
            r.next = tmp
            r = tmp
            result.length += 1
            tail = tail.next
        r.next = None
        return result

    def delstr(self, i, j):
        # 从串s中删去第i个字符开始的长度为j 的字串， 并返回产生的新串
        if i <= 0 or i > self.length:
            raise IndexError("Index is out!")
        result = LKString()
        r = result.L
        current = self.L.next
        for _ in range(i-1):
            tmp = Node(current.data)
            r.next = tmp
            r = tmp
            result.length += 1
            current = current.next
        for _ in range(j):
            current = current.next
        while current:
            tmp = Node(current.data)
            r.next = tmp
            r = tmp
            result.length += 1
            current = current.next
        r.next = None
        return result

    def repstr(self, i, j, lkstr):
        if i <= 0 or i > self.length or i + j - 1 > self.length:
            raise IndexError("Index is out of range!")
        result = LKString()
        r = result.L
        current = self.L.next
        for _ in range(i-1):
            tmp = Node(current.data)
            r.next = tmp
            r = tmp
            result.length += 1
            current = current.next
        for _ in range(j):
            current = current.next
        lkstr_cur = lkstr.L.next
        while lkstr_cur:
            tmp = Node(lkstr_cur.data)
            r.next = tmp
            r = tmp
            result.length += 1
            lkstr_cur = lkstr_cur.next
        while current:
            tmp = Node(current.data)
            r.next = tmp
            r = tmp
            result.length += 1
            current = current.next
        r.next = None
        return result


if __name__ == '__main__':
    ss = "abcdefghijklmn"
    test1 = LKString()
    test1.assign(ss)
    test1.show_str()
    test2 = LKString()
    test2.copy(test1)
    test2.show_str()
    ss2 = "abcde123"
    test3 = LKString()
    test3.assign(ss2)
    print test2.equal(test3)
    test4 = test3.contact(test2)
    test4.show_str()
    test5 = test4.substr(2, 5)
    test5.show_str()
    ss3 = "!!!!"
    tests = LKString()
    tests.assign(ss3)
    ss4 = "1234567890"
    tests2 = LKString()
    tests2.assign(ss4)
    test6 = test4.insstr(3, test5)
    test6.show_str()
    test7 = test6.delstr(3, 3)
    test7.show_str()
    test8 = tests2.repstr(3, 5, tests)
    test8.show_str()