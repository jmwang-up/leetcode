class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        n = len(candidates)
        res = []
        stack = []

        def back_strace(nums, start):

            if sum(stack) == target:
                res.append(stack)
                return

            if sum(stack) > target:
                return

            for i in range(n):

                stack.append(nums[i])
                back_strace(nums, i)
                stack.pop()

        back_strace(candidates, 0)
        return res