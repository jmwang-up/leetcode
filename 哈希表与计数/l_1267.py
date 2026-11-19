class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        rows = [0] * m
        colums = [0] * n

        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows[i] += 1
                    colums[j] += 1


        for i in range(m):
            for j in range(n):
                if rows[i] > 1 or colums[j] > 1:
                    res += 1

        return res