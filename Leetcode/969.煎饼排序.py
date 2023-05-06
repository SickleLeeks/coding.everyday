#!/usr/bin/env python
# encoding: utf-8
# Created by BIT09 at 2023/5/6
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []
        # 从数组长度为n开始遍历，直到可调整数组长度为1
        for n in range(len(arr), 1, -1):
            index = 0
            # 寻找当前数组对象的最大值位置
            for i in range(n):
                if arr[i] > arr[index]:
                    index = i
            # 如果最大值位置为n-1, 则跳过
            if index == n - 1:
                continue
            # 将最大值位置索引赋给m
            m = index
            # 第一步：选择index +1的，反转子数组
            for i in range((m + 1) // 2):
                arr[i], arr[m - i] = arr[m - i], arr[i]  # 原地反转
            # 第二步：选择当前数组对象长度为n，反转数组对象
            for i in range(n // 2):
                arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]  # 原地反转
            # 添加当前操作的索引位置 index +1
            ans.append(index + 1)
            # 添加当前反转的数组位置 n
            ans.append(n)
        return ans


if __name__ == '__main__':
    today = Solution()
    arr = list(map(int, input("arr = ").strip().split(',')))
    print(today.pancakeSort(arr))
