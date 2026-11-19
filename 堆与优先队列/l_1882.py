from typing import List
import heapq 

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        """
        每台服务器只能处理一项任务
        优先权重小的空闲服务器
        多台空闲服务器，选下标最小的
        """
        free_servers = [(v, i)for i, v in enumerate(servers)]
        heapq.heapify(free_servers)
        busy_heap = []
        # print(busy_heap)
        

        res = []
        for t, duration in enumerate(tasks):
            # 忙碌的服务器不为空, 需要看当前时间能不能用(预计空闲的时间，权重，索引)
            while busy_heap and t >= busy_heap[0][0]:
                heapq.heappush(free_servers, (busy_heap[0][1], busy_heap[0][2]))
                heapq.heappop(busy_heap)

            # 没有空闲的, 需要从忙碌的里面拿一个
            if not free_servers:
                # 必须从忙碌的里面哪一个
                start_time, weight, idx = heapq.heappop(busy_heap)
            else:
                weight, idx = heapq.heappop(free_servers)
                start_time = t

            res.append(idx)
            heapq.heappush(busy_heap, (duration+start_time, weight, idx))

        return res




if __name__ == '__main__':

    so = Solution()
    servers = [3,3,2]
    tasks = [1,2,3,2,1,2]
    print(so.assignTasks(servers, tasks))
    print(so.assignTasks([5,1,4,3,2], [2,1,2,4,5,2,1]))
    print(so.assignTasks([10,63,95,16,85,57,83,95,6,29,71], [70,31,83,15,32,67,98,65,56,48,38,90,5]))


