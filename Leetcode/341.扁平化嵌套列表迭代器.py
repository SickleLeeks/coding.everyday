#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 22:16
# @Author  : Alvaro Pang
# @File    : 341.扁平化嵌套列表迭代器.py
# @Software: PyCharm
from utils import NestedInteger


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop(-1).getInteger()

    def hasNext(self) -> bool:
        while len(self.stack) > 0 and self.stack[-1].isInteger() is False:
            self.stack += self.stack.pop().getList()[::-1]
        return len(self.stack) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
