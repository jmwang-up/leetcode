from collections import Counter

class Solution:
    def minSetBits(self, nums: list[int], k: int) -> int:

        n = len(nums)
        xi = []
        for i in range(n - k + 1):
            cur = nums[i]
            for j in range(k):
                cur &= nums[i + j]
            xi.append(cur)

        def count_and(val, vals:list) -> bool:

            for v in vals:
                if val & v == 0:
                    return False
            return True

        res = []
        for x in range(max(xi) + 1):
            if count_and(x, xi):
                res.append(bin(x)[2:])

        return -1 if not res else Counter(res[0])['1']



if __name__ == "__main__":

    so = Solution()
    # res = so.minSetBits([6,7,3], 2)
    # print(f"res:{res}")
    # res = so.minSetBits([3,5], 2)
    # print(f"res:{res}")

    res = so.minSetBits([5,8], 1)
    print(f"res:{res}")
    # res = so.minSetBits([2, 1], 2)
    # print(f"res:{res}")