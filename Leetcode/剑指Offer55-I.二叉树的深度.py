#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 22:44
# @Author  : Alvaro Pang
# @File    : 剑指Offer55-I.二叉树的深度.py
# @Software: PyCharm
from utils import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_height = 1 + self.maxDepth(root.left)
            right_height = 1 + self.maxDepth(root.right)
            return max(left_height, right_height)
