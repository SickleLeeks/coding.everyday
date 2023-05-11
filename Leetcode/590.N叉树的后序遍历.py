#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 22:56
# @Author  : Alvaro Pang
# @File    : 590.N叉树的后序遍历.py
# @Software: PyCharm
from typing import List


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []

        def traverse(node: 'Node'):
            if node is None:
                return
            for child in node.children:
                traverse(child)
            ans.append(node.val)

        traverse(root)
        return ans
