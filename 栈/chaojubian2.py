"""
序列的最大值，请你告诉他这个最大值区间期望值是多少
对于连续子序列的定义，例如长度为3序列为2 5 6, 他的
连续子序列有{2}, {5}, {6}, {2, 5}, {5, 6}, {2, 5, 6}

输入描述

第一行数字n表示序列长度
接下来一行n个数字来描述这个序列
1 <= n <= 100000
数字保证是正整数不超过100000

输出描述
一行一个数字表示答案, 表示这个最大值期望, 输出结果保留6为小数。

思路
找到左边第一个大于a[i]的数, 找到右边第一个大于等于a[i]的数，两边都是
"""
import sys


def solve():

    data = sys.stdin.read().split()
    n = int(data[0])
    a = [int(x) for x in data[1:1+n]]

    left = [0] * n
    stack = []

    for i in range(n):

        while stack and a[stack[-1]] <= a[i]:
            stack.pop()

        if stack:
            left[i] = stack[-1]
        else:
            left[i] = -1

        stack.append(i)

    right = [0] * n

    stack = []
    for i in range(n-1, -1, -1):

        while stack and a[stack[-1]] < a[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        else:
            right[i] = n

        stack.append(i)

    total = 0

    for i in range(n):
        cnt = (i - left[i]) * (right[i] - i)
        total += a[i] * cnt

    all_sub = n * (n + 1) // 2

    ans = total / all_sub
    print(f"totol:{total}, all_sub:{all_sub}")
    print("{0:.6f}".format(ans))    


if __name__ == "__main__":

    solve()