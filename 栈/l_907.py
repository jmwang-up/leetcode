from typing import list


class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:

        """
        给定一个整数数组 arr，找到 min(b) 的总和，其中 b 的范围为 arr 的每个（连续）子数组。
        由于答案可能很大，因此 返回答案模 10^9 + 7 。
        思考这个题目半个小时
        """

        """
        思路，查找每一个元素最左边第一个小于于等于他的元素和右边第一个小于他的元素
        """

        n = len(arr)
        left = [0] * n
        stack = []

        for i in range(n):
            # 左：栈中大于arr[i]的都弹出，因为我要找第一个小于arr[i]的元素
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)

        right = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # 右: 栈中大于等于arr[i]的都弹出, 因为我要右边第一个小于arr[i]的元素
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]
            else:
                right[i] = n

            stack.append(i)

        res = 0

        for i in range(n):

            cnt = (i - left[i]) * (right[i] - i)
            res += cnt * arr[i]

        return res

        