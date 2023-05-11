#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 23:21
# @Author  : Alvaro Pang
# @File    : 94.二叉树的中序遍历.py
# @Software: PyCharm
from typing import Optional, List

from utils import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            traverse(node.left)
            ans.append(node.val)
            traverse(node.right)

        traverse(root)
        return ans
