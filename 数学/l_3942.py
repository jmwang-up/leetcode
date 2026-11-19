class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        """
        [0,2,1] 0 2 1  -> 翻转 [1 2 0] -> 左移 [2 0 1]
        [0,2,1] -> 右移 [1 0 2]
        """
        # 然后看 n - 1 在0的左边还是右边
        """
        [3 0 1 2], 这个是n - 1在0的左边
        直接左旋 那就是start次
        如果是先翻转, 先把0移到末尾处, 然后在翻转
        [2 1 0 3] -> 左旋次数是n - start 然后再翻转一次 1 
        一共就是n - start + 2
        这个是n - 1在右边的情况
        """

        """
        [2 1 0 3], 这个是n - 1在0的右边
        先左旋 start + 1次, 然后反转1, 一共start + 2
        先反转 1次[3 0 1 2], 左旋 n - start - 1
        """

        n = len(nums)
        if n <= 1:
            return 0
        start = nums.index(0)

        asc = True
        desc = True

        for i in range(1, n):

            index = (start + i) % n
            # 说明是降序
            if nums[index] != i:
                asc = False

            if nums[index] != n - i:
                desc = False

            if not asc and not desc:
                return -1

        if asc:
            return min(start, n - start + 2)

        return min(start + 2, n - start)

   