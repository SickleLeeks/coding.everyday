#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 21:54
# @Author  : Alvaro Pang
# @File    : 99.恢复二叉搜索树.py
# @Software: PyCharm
from typing import Optional

from utils import TreeNode


class Solution:
    def recoverTree(self, root:Optional[TreeNode]) -> None:
        self.pre, self.first, self.second = None, None, None
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val > root.val:
                    if not self.first:
                        self.first = self.pre
                    self.second = root
                self.pre = root
            inOrder(root.right)
        inOrder(root)
        self.first.val, self.second = self.second.val, self.first.val
