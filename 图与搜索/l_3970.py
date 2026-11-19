from heapq import heappop, heappush

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        """
        思路就是使用xxx算法, 每次讲权重
        """
        # 先把图转换成根据u可遍历的结构
        graphs = [[] for _ in range(n)]

        for u, v, w in edges:
            graphs[u].append((v, w))

        dist = [[inf] * (k + 1) for _ in range(n)]
        # cost u count
        heap = [(0, 0, 1)]

        while heap:

            cost, u, count = heappop(heap)

            if cost > dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, w in graphs[u]:

                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + w

                if new_cost < dist[v][new_count]:
                    heappush(heap, (new_cost, v, new_count))

        return -1





        