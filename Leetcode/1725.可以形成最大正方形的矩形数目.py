#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 23:24
# @Author  : Alvaro Pang
# @File    : 1725.可以形成最大正方形的矩形数目.py
# @Software: PyCharm
from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen, count = 0, 0
        for i, rectangle in enumerate(rectangles):
            k = min(rectangle[0], rectangle[1])
            if k > maxLen:
                maxLen = k
                count = 1
            elif k == maxLen:
                count += 1
            else:
                continue
        return count
