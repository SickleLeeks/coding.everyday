#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 23:24
# @Author  : Alvaro Pang
# @File    : 117.填充每个节点的下一个右侧节点指针II.py
# @Software: PyCharm

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        cur = root
        while cur:
            dummyHead = Node(-1)  # 为下一行的之前的节点，相当于下一行所有节点链表的头节点
            pre = dummyHead  # 指向当前的虚拟节点
            while cur:
                if cur.left:  # 如果当前节点有左子树, 将指针移动到左子树上
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:  # 如果当前节点有右子树， 将指针一定到右子树上
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next  # 移动当前节点位置
            cur = dummyHead.next  # 此处为换行操作，更新到下一行
        return root
