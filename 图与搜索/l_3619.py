from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:


        m = len(grid)
        n = len(grid[0])
        self.res = 0
        def dfs(rows, colums):

            if rows < 0 or colums < 0 or rows >= m or colums >= n:
                return

            self.cost += grid[rows][colums]
            grid[rows][colums] = 0

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for x, y in directions:
                dfs(rows + x, colums + y)

        for i in range(m):
            for j in range(n):

                self.cost = 0
                if grid[i][j] != 0:
                    dfs(i, j)

                    if self.cost % k == 0:
                        self.res += 1
        return self.res




            