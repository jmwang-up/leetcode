class Solution:
    def findMin(self, nums: list[int]) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (r + l) // 2
            #说明最小值在左边
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1

        return nums[l]


if __name__ == "__main__":

    nums = [3,4,5,1,2]

    so = Solution()
    print(so.findMin(nums))