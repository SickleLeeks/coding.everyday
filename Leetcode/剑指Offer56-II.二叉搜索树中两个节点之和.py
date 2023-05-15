#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 22:48
# @Author  : Alvaro Pang
# @File    : 剑指Offer56-II.二叉搜索树中两个节点之和.py
# @Software: PyCharm
from utils import TreeNode


class Solution:
    def __init__(self):
        self.s = set()

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root is None:
            return False
        if k - root.val in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
