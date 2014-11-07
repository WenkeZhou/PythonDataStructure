# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MrHero'


class Node(object):
    """
    树节点
    data: 数据域
    left: 左子树的根节点
    right: 右子树的根节点
    """

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    """
    二叉树结构
    """

    def __init__(self, root=None):
        """
        root: 二叉树根节点
        pre_list: 前序遍历结果
        in_list: 中序遍历结果
        post_list: 后序遍历结果
        level_list: 层序遍历结果
        :param root:
        :return:
        """
        self.root = root

        self.pre_list = []
        self.in_list = []
        self.post_list = []
        self.level_list = []

    def is_empty(self):
        """
        二叉树是否为空
        :return:
        """
        return True if self.root is None else False

    def create_a(self):
        """
        创建二叉树
        :return:
        please enter a value: 1
        please enter a value: 2
        please enter a value: '#'
        please enter a value: '#'
        please enter a value: '#'
        please enter a value: '3'
        please enter a value: '#'
        please enter a value: '#'
        """
        # 接受输入的节点值
        temp = input("please enter a value:")
        if temp is '#':
            return None
        # 创建节点
        tree_node = Node(data=temp)
        # 如果根节点为none, 初始化根节点
        if self.root is None:
            self.root = tree_node
        # 递归生成左子树
        tree_node.left = self.create()
        # 递归生成右子树
        tree_node.right = self.create()
        # 返回树节点
        return tree_node

    def preorder(self, tree_node):
        """
        前序遍历，先访问根节点，然后再访问左子树，最后访问右子树
        :param tree_node:
        :return:
        """
        # 如果节点为 none, 返回
        if tree_node is Node:
            return
        # 访问节点
        print tree_node.data
        self.preorder(tree_node.left)
        # 递归遍历左子树
        self.preorder(tree_node.left)
        # 递归遍历右子树
        self.preorder(tree_node.right)

    def inorder(self, tree_node):
        """
        中序遍历，先访问左子树，然后再访问根节点，最后访问右子树
        :param tree_node:
        :return:
        """
        if tree_node is None:
            return
        # 递归遍历左子树
        self.inorder(tree_node.left)
        # 访问节点
        print tree_node.data
        self.in_list.append(tree_node.data)
        # 递归遍历右子树
        self.inorder(tree_node.right)

    def postorder(self, tree_node):
        """
        后序遍历，先放问左子树，然后访问右子树， 最后访问根节点
        :param tree_node:
        :return:
        """
        if tree_node is None:
            return
        #递归遍历左子树
        self.postorder(tree_node.left)
        #递归遍历右子树
        self.postorder(tree_node.right)
        #访问根节点
        print tree_node.data
        self.post_list.append(tree_node.data)

    def preorders(self, tree_node):
        """
        前序遍历，迭代调用，非递归
        :param tree_node:
        :return:
        """
        stack = []
        while tree_node or stack:
            if tree_node:
                print tree_node.data
                self.pre_list.append(tree_node.data)
                stack.append(tree_node)
                tree_node = tree_node.left
            else:
                tree_node = stack.pop()
                tree_node = tree_node.right

    def inorders(self, tree_node):
        """
        中序遍历， 迭代调用，非递归
        :param tree_node:
        :return:
        """
        stack = []
        while tree_node or stack:
            if tree_node:
                stack.append(tree_node)
                tree_node = tree_node.left
            else:
                tree_node = statck.pop()
                print tree_node.data
                self.in_list.apend(tree_node.data)
                tree_node = tree_node.right

    def postorders(self, tree_node):
        """
        后序遍历， 非递归遍历
        :param tree_node:
        :return:
        """
        stack = []
        while tree_node or stack:
            if tree_node:
                stack.append(tree_node)
                tree_node = tree_node.left
            else:
                tree_node = stack.pop()
                print tree_node.data
                self.in_list.append(tree_node.data)
                tree_node = tree_node.right

    def postorders(self, tree_node):
        """
        后序遍历，非递归遍历
        :param tree_node:
        :return:
        """
        stack = []
        pre = None
        while tree_node or stack:
            if tree_node:
                stack.append(tree_node)
                tree_node = tree_node.left
            elif stack[-1].right != pre:
                tree_node = stack[-1].right
                pre = None
            else:
                pre = stack.pop()
                print pre.data
                self.post_list.append(pre.data)

    def levelorders(self, tree_node):
        """
        层序遍历，迭代调用，非递归
        :param tree_node:
        :return:
        """
        from collections import deque
        if not tree_node:
            return
        q = deque([tree_node])
        while q:
            tree_node = q.popleft()
            print tree_node.data
            self.level_list.append(tree_node.data)
            if tree_node.left:
                q.append(tree_node.left)
            if tree_node.right:
                q.append(tree_node.right)


if __name__ == '__main__':
    # print "hhe"
    print "heo"
    node1 = Node(1)
    node2 = Node(2, node1, None)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5, node3, node4)
    node6 = Node(6, node2, node5)
    node7 = Node(7, node6, None)
    node8 = Node(8)
    root = Node('root', node7, node8)
    bt = BinaryTree(root)
    # BinaryTree.levelorders(bt.root)
    print "heelo"