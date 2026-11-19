import heapq
from collections import defaultdict
class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        
        """
        服务器信息：
        同时处理多个请求组
        不能同时处理超过一个请求
        """
        n = len(arrival)
        free_servers = [0] * k
        res = [0] * k
        # for i in range(k):
        #     free_servers.append(i)

        busy_servers = []
        heapq.heapify(busy_servers)

        for i in range(n):
            while busy_servers:

                end_time = busy_servers[0][0]
                if arrival[i] <= end_time:
                    break

                servers = heapq.heappop(busy_servers)

                idx = servers[1]
                free_servers[idx] = 0

            if len(busy_servers) == k:
                continue

            time = load[i] + arrival[i]
            index = i % k

            for j in range(k):
                index = (i + j) % k
                if free_servers[index] == 0:
                    heapq.heappush(busy_servers, (time, index))
                    free_servers[index] = 1
                    res[index] += 1

        print(res)
        max_num = max(res)
        total = []
        for i, v in enumerate(res):
            if v == max_num:
                total.append(i)
        

        return total


if __name__ == "__main__":

    so = Solution()
    # res = so.busiestServers(3, [1,2,3,4,5], [5,2,3,3,3])
    # print(res)

    # res = so.busiestServers(3, [1,2,3,4], [1,2,1,2])
    # print(res)

    # res = so.busiestServers(3, [1,2,3], [10,12,11])
    # print(res)

    res = so.busiestServers(3, [1,2,3,4,8,9,10], [5,2,10,3,1,2,2])
    print(res)
        

