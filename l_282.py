class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:

        res = []
        n = len(num)
        def back_strace(path, index, mul, post):

            if index == n and mul == target:
                res.append(path)
                return

            for i in range(index, n):
                cur_str = num[index, i + 1]
                cur = int(cur_str)

                if index == 0:
                    back_strace(path + cur_str, i + 1, cur, cur)
                else:
                    # 选择加减乘除
                    back_strace(path + cur_str, i + 1, mul + cur, cur)
                    back_strace(path + cur_str, i + 1, mul - cur, -cur)

                    back_strace(path + cur_str, i + 1, (mul - post) + (cur * post) , cur * post)

        back_strace("", 0, 0, 0)
        return res