
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        """
        要用bfs解，因为题目是腐烂的橘子同时在每一分钟时腐烂周围的橘子，分钟数就是bfs时的层数。

        1. 首先找出初始的腐烂的橘子, 加入到队列中。
        2. 遍历队列中的格子, 将新鲜的橘子腐烂掉, 然后存入队列中
        """

        m = len(grid)
        n = len(grid[0])
        # print(f"grid:{grid}")
        fresh = 0

        quene = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    quene.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
    
        # print(f"fresh:{fresh}")

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
        minutes = 0
        while quene and fresh > 0:

            for _ in range(len(quene)):
                i, j = quene.popleft()
                # print(f"i:{i}, j:{j}")
                for x, y in directions:
    
                    n_i = x + i
                    n_j = y + j

                    if n_i < 0 or n_j < 0 or n_i >= m or n_j >= n:
                        continue

                    if grid[n_i][n_j] == 1:
                        grid[n_i][n_j] = 2
                        fresh -= 1
                        quene.append((n_i, n_j))

            minutes += 1
        print(f"minutes:{minutes}, fresh:{fresh}")
        if fresh == 0:
            return minutes
        return -1



if __name__ == "__main__":

    so = Solution()

    for case in [[[2,1,1],[1,1,0],[0,1,1]], [[2,1,1],[0,1,1],[1,0,1]], [[0,2]]]:
        res = so.orangesRotting(case)
        print(res)