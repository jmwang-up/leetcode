class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (r + l) // 2

            if target == nums[mid]:
                return mid

            # 先确定在哪一段单调递增区间
            if nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

if __name__ == "__main__":

    so = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(so.search(nums, target))