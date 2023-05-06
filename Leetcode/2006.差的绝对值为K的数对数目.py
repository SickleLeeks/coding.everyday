#!/usr/bin/env python
# encoding: utf-8
# Created by BIT09 at 2023/5/6
import sys
from typing import List
from collections import Counter


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ## 暴力法
        # res, n = 0, len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if abs(nums[i] - nums[j]) == k:
        #             res += 1
        # return res
        ## 哈希表 + 一次遍历
        res = 0
        cnt = Counter()
        for num in nums:
            # 对于每个元素，只需要知道在这个之前符合条件的i的个数
            res += cnt[num - k] + cnt[num + k]
            cnt[num] += 1
        return res


if __name__ == '__main__':
    today = Solution()
    nums = list(map(int, input('nums = ').strip().split(',')))
    k = int(input('k = '))
    print(today.countKDifference(nums, k))
