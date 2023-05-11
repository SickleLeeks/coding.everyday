#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 22:48
# @Author  : Alvaro Pang
# @File    : 589.N叉树的前序遍历.py
# @Software: PyCharm
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def traverse(node: 'Node'):
            if node is None:
                return
            res.append(node.val)
            for child in node.children:
                traverse(child)

        traverse(root)
        return res
