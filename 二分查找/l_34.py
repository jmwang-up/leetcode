class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        res = []

        n = len(nums)
        l, r = 0, n - 1
        res1, res2 = -1, -1
        while l <= r:

            mid = (r + l) // 2
            # print(f"l:{l}, r:{r}, mid:{mid}")
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                res1 = mid
                r = mid - 1


        l, r = 0, n - 1
        while l <= r:
            mid = (r + l) // 2
            # print(f"l:{l}, r:{r}, mid:{mid}")
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                res2 = mid
                l = mid + 1
        return [res1, res2]


if __name__ == '__main__':

    so = Solution()
    res = so.searchRange([5,7,7,8,8,10], 8)
    print(res)