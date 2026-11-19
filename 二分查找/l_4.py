class Solution:
    def findMedianSortedArrays(
        self, nums1: list[int], nums2: list[int]
    ) -> float:

        # 保证 nums1 是较短的数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        left, right = 0, m

        while left <= right:
            # nums1 的分割位置
            i = (left + right) // 2

            # nums2 的分割位置
            j = (m + n + 1) // 2 - i

            # 分割线两侧的四个元素
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')

            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # nums1 左侧最大元素太大
            if left1 > right2:
                right = i - 1

            # nums1 右侧最小元素太小
            elif left2 > right1:
                left = i + 1

            # 找到正确划分
            else:
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                return (
                    max(left1, left2) + min(right1, right2)
                ) / 2




if __name__ == '__main__':

    so = Solution()
    nums1 = [1,2]
    nums2 = [3,4]
    print(so.findMedianSortedArrays(nums1, nums2))