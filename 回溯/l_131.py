class Solution:
    def partition(self, s: str) -> list[list[str]]:

        n = len(s)
        res, path = [], []

        def back_strace(start, path):
            if start == n:
                res.append(path[:])
                return

            for i in range(start, n):
                # print(f"start:{start} -> i:{ i + 1}")
                part = s[start:i + 1]
                if part == part[::-1]:
                    path.append(part)

                    back_strace(i + 1, path)
                    path.pop()

        back_strace(0, path)
        return res

if __name__ == '__main__':

    so = Solution()
    print(so.partition('aab'))
