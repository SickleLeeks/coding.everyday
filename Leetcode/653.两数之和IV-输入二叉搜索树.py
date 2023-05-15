#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 22:33
# @Author  : Alvaro Pang
# @File    : 653.两数之和IV-输入二叉搜索树.py
# @Software: PyCharm
from typing import Optional

from utils import TreeNode


class Solution:
    def __init__(self):
        self.s = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        if k - root.val in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
