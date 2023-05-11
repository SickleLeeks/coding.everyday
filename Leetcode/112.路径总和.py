#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 23:11
# @Author  : Alvaro Pang
# @File    : 112.路径总和.py
# @Software: PyCharm
from typing import Optional

from utils import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
