class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        res = []
        stack = []

        n = len(nums)
        used = [False] * n

        def back_strace(nums):
            # 终止条件
            if len(stack) == len(nums):
                res.append(stack[:])
                return


            for i in range(n):

                if used[i] == False:
                    continue

                stack.append(nums[i])
                used[i] = True

                back_strace(nums)

                stack.pop()
                used[i] = False

        back_strace(nums)
        return res

