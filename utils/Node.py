#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 22:48
# @Author  : Alvaro Pang
# @File    : Node.py
# @Software: PyCharm

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
