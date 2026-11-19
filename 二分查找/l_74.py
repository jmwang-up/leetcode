class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        # 先确定在哪一行

        m, n = len(matrix), len(matrix[0])

        l, r = 0, m - 1

        while l <= r:
            print(f"l:{l}, r:{r}")
            mid = (r + l) // 2
            #小于最小值, 说明在前面的行，说明要缩小mid
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][n - 1]:
                l = mid + 1
            else:
                # 找到对应的行了, 再次二分
                
                sub_l, sub_r = 0, n - 1
                sub_mid = (sub_r + sub_l) // 2
                while sub_l <= sub_r:
                    # 小于mid值, 说明调整
                    if target < matrix[mid][sub_mid]:
                        sub_l = sub_mid + 1
                    elif target > matrix[mid][sub_mid]:
                        sub_r = sub_mid - 1
                    else:
                        return True
        return False



if __name__ == "__main__":

    so = Solution()
    print(so.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))