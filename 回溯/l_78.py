class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        res, stack = [], []

        n = len(nums)

        def back_trace(nums, start):

            res.append(stack[:])

            if start == len(nums):
                return

            for i in range(start, n):

                res.append(nums[i])

                back_trace(nums, i + 1)

                res.pop()

        back_trace(nums, 0)
        return res