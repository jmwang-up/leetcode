from typing import List

class Solution:
    """
    leetcode solution
    """
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        """
        check arith metic subarray
        """
        # 1、判断子数组是否是等差数列，最大值 - 最小值 // l - r 能否整除
        # 2、最大值 - 最小值 等于0, 也是等差数列

        res = []

        for left, right in zip(l, r):

            minv = min(nums[left:right + 1])
            maxv = max(nums[left:right + 1])

            # 最大值和最小值相等 说明是等差数列
            if maxv - minv == 0:
                res.append(True)
                continue

            # 不能整除 说明不是等差数列
            if (maxv - minv) % (right - left) != 0:
                res.append(False)
                continue

            # 公差
            d = (maxv - minv) // (right - left)

            seen = set()
            flag = True
            for num in nums[left:right + 1]:

                if (num - minv) % d != 0:
                    flag = False
                    continue

                # 能够整除
                t = (num - minv) // d
                if t in seen:
                    flag = False
                    continue

                seen.add(t)

            res.append(flag)

        return res


