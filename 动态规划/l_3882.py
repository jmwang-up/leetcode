class Solution:
    def minCost(self, grid: list[list[int]]) -> int:

        """
        dfs超时了, 
        """


        m = len(grid)
        n = len(grid[0])

        dp = [[set() for _ in range(n) ]for _ in range(m)]

        dp[0][0] = 0

        for i in range(m):
            for j in range(n):

                # 从上方过来
                if i > 0:
                    dp[i][j].add(dp[i - 1][j] ^ grid[i][j])

                # 从右边过来
                if j > 0:
                    dp[i][j].add(dp[i][j - 1] ^ grid[i][j])

        return min(dp[m - 1][n - 1])
