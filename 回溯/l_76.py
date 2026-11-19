class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        stack = []
        res = []
        n = len(nums)

        def back_strace(nums, start):

            if len(stack) == n:
                res.append(stack[:])
                return

            for i in range(start, n):

                stack.append(nums[i])

                back_strace(nums, i + 1)

                stack.pop()

        return res
