from typing import List



class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        n = len(num)
        ans = []

        def backtrack(expr:str, index: int, res: int, mul: int):

            if index == n:
                if res == target:
                    ans.append(expr)
                return

            for i in range(index, n):
                if i > index and num[index] == '0':
                    break 
                cur_str = num[index: i + 1]
                print(f"cur_str:{cur_str}")
                cur = int(cur_str)

                if index == 0:
                    backtrack(cur_str , i + 1, cur, cur)
                else:
                    # 尝试加号
                    backtrack(expr + '+' + cur_str, i + 1, res + cur, cur)
                    # 尝试减号
                    backtrack(expr + '-' + cur_str, i + 1, res - cur, -cur)
                    # 尝试乘法
                    backtrack(expr + '*' + cur_str, i + 1, (res - mul) + (cur * mul), mul * cur )


        backtrack('', 0, 0, 0)
        return ans


if __name__ == "__main__":

    so = Solution()
    for case, target in zip(["105", "123"], [5,6]):
        ans = so.addOperators(case, target)
        print(ans)