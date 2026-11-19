from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        # queries.sort()
        logs.sort(key=lambda x:x[1])
        new_queries = sorted(enumerate(queries), key = lambda x:x[1])
        print(new_queries)

        res = [0] * len(queries)
        count = [0] * (n + 1)
        # print(count)
        l, r = 0, 0
        # 当前窗口内，收到过请求的服务器数量
        active_servers = 0
        for ori_index, query in new_queries:

            while r < len(logs) and logs[r][1] <= query:
                server_id = logs[r][0]
                if count[server_id] == 0:
                    active_servers += 1
                count[server_id] += 1
                r += 1
            # print(count)
            while l < r and logs[l][1] < query - x:
                server_id = logs[l][0]
                count[server_id] -= 1
                if count[server_id] == 0:
                    active_servers -= 1
                l += 1
            # print(count)
            res[ori_index] = n - active_servers
        return res

if __name__ == "__main__":

    so = Solution()
    print(so.countServers(3, [[1,3],[2,6],[1,5]], 5, [11,10]))

            
