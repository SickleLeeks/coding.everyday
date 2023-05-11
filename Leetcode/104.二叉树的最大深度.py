#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 23:01
# @Author  : Alvaro Pang
# @File    : 104.二叉树的最大深度.py
# @Software: PyCharm
from typing import Optional

from utils import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1
