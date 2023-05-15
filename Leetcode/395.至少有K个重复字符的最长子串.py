#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 21:35
# @Author  : Alvaro Pang
# @File    : 395.至少有K个重复字符的最长子串.py
# @Software: PyCharm

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


if __name__ == '__main__':
    today = Solution()
    s = input('s = ').strip()
    k = int(input('k = ').strip())
    print(today.longestSubstring(s=s, k=k))
