from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:

        n = len(nums)
        pre = [0] * (n + 1)

        for i in range(n):
            pre[i + 1] = nums[i] + pre[i]

        res = float('inf')

        for start in range(len(pre)):

            for i in range(l, r + 1):
                res = min(sum(pre[i : i+start]), res)

        return res