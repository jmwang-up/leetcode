from math import gcd,lcm
from typing import List

class Solution:
    def maxLength(self, nums: List[int]) -> int:        
        res = 0
        n = len(nums)

        for i in range(n):

            prod_val = nums[i]
            lcm_val = nums[i]
            gcd_val = nums[i]

            for j in range(i + 1,n):

                gcd_val = gcd(gcd_val, nums[j])
                lcm_val = lcm(lcm_val, nums[j])
                prod_val *= nums[j]

                if prod_val == lcm_val * gcd_val:
                    res = max(res, j - i + 1)
                    # print(i, j)
        return res


if __name__ == "__main__":

    so = Solution()
    res = so.maxLength([1,2,1,2,1,1,1])
    print(res)