
import heapq


class SlidingMedian:
    def __init__(self, n):
        self.low = []     # 最大堆：(-value, index)
        self.high = []    # 最小堆：(value, index)
        self.deleted = [False] * n
        self.where = [-1] * n

        self.low_size = self.high_size = 0
        self.low_sum = self.high_sum = 0

    def prune(self, heap):
        # 惰性删除失效的堆顶元素
        while heap and self.deleted[heap[0][1]]:
            heapq.heappop(heap)

    def balance(self):
        self.prune(self.low)
        self.prune(self.high)

        # 保证 low 的有效元素数量等于 high
        # 或比 high 多 1
        if self.low_size > self.high_size + 1:
            neg_v, idx = heapq.heappop(self.low)
            v = -neg_v
            self.low_size -= 1
            self.low_sum -= v

            heapq.heappush(self.high, (v, idx))
            self.high_size += 1
            self.high_sum += v
            self.where[idx] = 1
            self.prune(self.low)

        elif self.low_size < self.high_size:
            v, idx = heapq.heappop(self.high)
            self.high_size -= 1
            self.high_sum -= v

            heapq.heappush(self.low, (-v, idx))
            self.low_size += 1
            self.low_sum += v
            self.where[idx] = 0
            self.prune(self.high)

    def add(self, v, idx):
        self.prune(self.low)

        if not self.low or v <= -self.low[0][0]:
            heapq.heappush(self.low, (-v, idx))
            self.low_size += 1
            self.low_sum += v
            self.where[idx] = 0
        else:
            heapq.heappush(self.high, (v, idx))
            self.high_size += 1
            self.high_sum += v
            self.where[idx] = 1

        self.balance()

    def remove(self, v, idx):
        self.deleted[idx] = True

        if self.where[idx] == 0:
            self.low_size -= 1
            self.low_sum -= v
        else:
            self.high_size -= 1
            self.high_sum -= v

        self.where[idx] = -1
        self.balance()

    def cost(self):
        self.prune(self.low)
        median = -self.low[0][0]

        left = median * self.low_size - self.low_sum
        right = self.high_sum - median * self.high_size
        return left + right


class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        maritovexi = nums
        n = len(nums)

        # 第一阶段：计算每个长度 x 窗口的成本
        median = SlidingMedian(n)
        cost = []

        for i, v in enumerate(nums):
            median.add(v, i)

            if i >= x:
                median.remove(nums[i - x], i - x)

            if i >= x - 1:
                cost.append(median.cost())

        # 第二阶段：DP，选择 k 个不重叠窗口
        INF = float("inf")

        # 选择 0 个窗口时，成本为 0
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                # 不选以 i-1 结尾的窗口
                curr[i] = curr[i - 1]

                # 选以 i-1 结尾的窗口
                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + cost[i - x]
                    )

            prev = curr

        return prev[n]
