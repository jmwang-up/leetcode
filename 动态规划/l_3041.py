class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        """
        """
        dp = {}
        nums.sort()

        for x in nums:
            # 如果不加1，作为最后一个数，最长序列长度是多少
            dp[x] = max(dp.get(x, 0), dp.get(x - 1, 0) + 1)
            # 如果加一作为最后一个数，最长序列长度是多少
            dp[x + 1] = max(dp.get(x+1, 0), dp.get(x, 0) + 1 )

        return max(dp.values())