class Solution:
    def minCost(self, nums: list[int]) -> int:

        """
        对于每一个元素 先前缀 再后缀, 
        """
        n = len(nums)
        res = []
        """
        i = 3, 3 * 6
        """
        for i in range(1, n - 1):
            pre_cost = i * nums[i]
            post_cost = (n - i - 1) * nums[i]
            res.append(pre_cost + post_cost)
        print(res)
        return min(res)


if __name__ == "__main__":

    so = Solution()
    so.minCost([3,3,3,6,3,3])