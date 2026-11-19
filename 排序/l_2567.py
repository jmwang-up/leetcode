class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        
        """
        1 3 4
        1 4 5 7 8
        """
        n = len(nums)
        nums.sort()

        return min(nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0])