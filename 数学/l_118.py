class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        if numRows == 1:
            res = []
            first_rows = [1]
            res.append(first_rows)
            return res


        res = self.generate(numRows - 1)

        pre_rows = res[-1]

        cur_rows = [1]
        for i in range(len(pre_rows) - 1):
            cur_rows.append(pre_rows[i] + pre_rows[i + 1])
        cur_rows.append(1)

        res.append(cur_rows)
        return res




if __name__ == "__main__":

    so = Solution()
    print(so.generate(5))