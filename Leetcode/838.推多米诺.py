#!/usr/bin/env python
# encoding: utf-8
# Created by BIT09 at 2023/5/6
from collections import deque


class Solution:
    # 广度优先搜索
    def pushDominoes_method1(self, dominoes: str) -> str:
        n = len(dominoes)
        q = deque()
        time = [-1] * n
        force = [[] for _ in range(n)]
        # 遍历初始状态下的受力情况及位置
        for i, f in enumerate(dominoes):
            if f != '.':
                q.append(i)  # 队列中添加骨牌受力的位置, Add an element to the right side of the deque
                time[i] = 0  # 将该位置的时刻记为0
                force[i].append(f)  # 将该位置的受力方向添加到数组中
        res = ['.'] * n
        while q:
            i = q.popleft()  # Remove and return the leftmost element
            if len(force[i]) == 1:  # 如果当前位置有受力, 获取受力值，并修改res
                res[i] = f = force[i][0]
                # 如果力为向左，则下一个考虑的位置索引为i-1, 否则为i+1
                next_i = i - 1 if f == 'L' else i + 1
                if 0 <= next_i < n:
                    t = time[i]  # 当前受力时刻
                    if time[next_i] == -1:  # 如果next_i还没有受力
                        q.append(next_i)  # 队列中增加next_i的索引
                        time[next_i] = t + 1  # 修改对应的受力时刻
                        force[next_i].append(f)  # 增加其受力的方向
                    elif time[next_i] == t + 1:  # 如果next_i已经受力
                        force[next_i].append(f)
        return ''.join(res)

    # 模拟
    def pushDominoes_method2(self, dominoes: str) -> str:
        s = list(dominoes)
        n, i, left = len(s), 0, 'L'  # # 默认假设最左则存在向左倒的骨牌
        while i < n:  # 从最左侧位置开始遍历
            j = i
            while j < n and s[j] == '.':  # 找到一段连续的没有被推动的骨牌，直到s[j]不是'.'
                j += 1
            right = s[j] if j < n else 'R'  # 如果j<n,就把s[j]的值赋给right, 否则假设存在一块向右倒的骨牌

            if left == right:  # 方向相同，那么竖立的骨牌倒向同一个方向
                while i < j:
                    s[i] = right
                    i += 1
            elif left == 'R' and right == 'L':  # 方向相对，那么就从两侧向中间倒
                k = j - 1
                while i < k:
                    s[i] = 'R'
                    s[k] = 'L'
                    i += 1
                    k -= 1
            # 更新完成之后，将右侧倒向设置为left的值，并从j+1的位置开始新一轮遍历
            left = right
            i = j + 1
        return ''.join(s)


if __name__ == '__main__':
    today = Solution()
    dominoes = input("dominoes = ").strip()
    print(today.pushDominoes_method1(dominoes))
    print(today.pushDominoes_method2(dominoes))
