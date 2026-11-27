from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        # 状态转移公式用f(i) 表示 花费了i之后，买到的物品个数

        # 因为只有第一次买才会免费奖励，所以先用动态规划的思路把买第一遍的个数计算出来

        # 然后再用剩余的预算去买价格最便宜的

        dp = [0] * (budget + 1)

        min_price = min(price for _, price in items)

        for factor, price in items:

            cnt = 0
            for other_factor, _ in items:
                if other_factor % factor == 0:
                    cnt += 1

            for j in range(budget, price - 1, -1):

                dp[j] = max(dp[j - price] + cnt, dp[j])

        return max(dp[j] + (budget - j) // min_price for j in range(budget + 1))
