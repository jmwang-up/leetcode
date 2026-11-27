from typing import List
from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        base1, mod1 = 100003, 10**9 + 7
        base2, mod2 = 100019, 10**9 + 9 


        def check(k: int):
            # 目的：检查数据为k的窗口是否唯一
            # 任务：计算每个窗口的哈希值
            # 怎么做：使用滑动哈希的算法, 
            # 先计算123的哈希， 
            # 如果窗口移动到234, h(123) - ( out_num(1) * weight(10 **(3 - 1)) )

            # 每次移出去的都是最左边的, 所以权重是base1的k-1次方
            weight1 = pow(base1, k - 1, mod1)
            weight2 = pow(base2, k - 1, mod2)

            # 计算第一个窗口[0, k]的哈希
            hash1 = hash2 = 0
            for i in range(k):

                hash1 = (hash1 * base1 + nums[i]) % mod1
                hash2 = (hash2 * base2 + nums[i]) % mod2

            counts = Counter()
            counts[(hash1, hash2)] = 1

            # 处理窗口的移动
            for i in range(k, n):

                outgoing = nums[i - k]
                incoming = nums[i]

                hash1 = ((hash1 - outgoing * weight1) * base1 + incoming) % mod1
                hash2 = ((hash2 - outgoing * weight2) * base2 + incoming) % mod2

            counts[(hash1, hash2)] += 1
            return 1 in counts.values


        l, r = 1, n

        # 检查长度为k的子数组是否唯一, 如果唯一, 缩小窗口，如果不唯一，扩大窗口
        while l < r:

            mid = (r + l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l
