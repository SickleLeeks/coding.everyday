#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/15 22:56
# @Author  : Alvaro Pang
# @File    : 747.至少是其他数字两倍的最大数.py
# @Software: PyCharm
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # num = list(set(nums))
        # if len(num) <= 1:
        #     return 0
        # num.sort(reverse=True)
        # if num[0] < 2 * num[1]:
        #     return -1
        # return nums.index(num[0])

        m1, m2, idx = -1, -1, 0
        for i, num in enumerate(nums):
            if num > m1:
                m1, m2, idx = num, m1, i
            elif num > m2:
                m2 = num
        return idx if m1 >= m2 * 2 else -1


if __name__ == '__main__':
    today = Solution()
    nums = list(map(int, input('nums=').strip().split(',')))
    print(today.dominantIndex(nums))
