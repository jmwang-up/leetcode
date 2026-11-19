class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        """
        给定一个仅包含数字 0-9 的字符串 num 和一个目标值整数 target ，在 num 的数字之间添加 二元 运算符（不是一元）+、- 或 * ，返回 所有 能够得到 target 的表达式。

        注意，返回表达式中的操作数 不应该 包含前导零。

        注意，一个数字可以包含多个数位。
        """

        """
        使用回溯算法，每个数字可以选择 + - *, 回溯就是一种暴力遍历, 每一步选择决策项。
        """

        n = len(num)
        res = []

        def back_track(path:str, index:int, mul:int, post:int):

            # 终止条件
            if index == n and mul == target:
                res.append(path)
                return


            for i in range(index, n):

                if i > index and num[index] == '0':
                    # 规避01 02 02这种情况
                    break
                cur_str = num[index:i + 1]
                cur = int(cur_str)

                if index == 0:

                    back_track(cur_str, index + 1, cur, post)
                else:
                    # 依次选择 + - *

                    back_track(path + '+' + cur_str, i + 1, mul + cur, cur)

                    back_track(path + '-' + cur_str, i + 1, mul - cur, -cur)

                    # 1 + 2 * 3 这种情况, 传进来的mul是3 cur 2, 把1计算处理, (mul - post) + post * cur 

                    back_track(path + '*' + cur_str, i + 1, (mul - post) + post * cur, post * cur)

        back_track("", 0, 0, 0)
        return res


