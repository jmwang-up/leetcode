class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        n = len(nums)
        ans = []
        def back_strace(path, index, eval):

            if index == n:
                if eval == target:
                    ans.append(path)
                return

            cur = nums[index]
             
            back_strace(path + "-" + str(cur), index + 1, eval - nums[index])
            back_strace(path + "+" + str(cur), index + 1, eval + nums[index])


        back_strace("" , 0, 0)
        return len(ans)

if __name__ == "__main__":
    so = Solution()

    res = so.findTargetSumWays([1,1,1,1,1], 3)
    print(f"res:{res}")