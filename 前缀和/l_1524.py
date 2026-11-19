class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        

        total = 0
        # 偶数 奇数
        even, odd = 1, 0
        res = 0

        for x in arr:

            total += x

            if total % 2 == 0:
                even += 1
            else:
                odd += 1

            if total % 2 == 0:
                res += odd
            else:
                res += even
    
        return res % (10**9 + 7)
