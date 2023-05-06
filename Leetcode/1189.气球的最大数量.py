#!/usr/bin/env python
# encoding: utf-8
# Created by BIT09 at 2023/5/6

# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # 统计"a","b","1","o","n"的数量，返回其最小值即可
        cnt = Counter(c for c in text if c in 'balon')
        cnt['l'] //= 2
        cnt['o'] //= 2
        return min(cnt.values()) if len(cnt) == 5 else 0


if __name__ == '__main__':
    today = Solution()
    text = input('text = ').strip()
    print(today.maxNumberOfBalloons(text))
