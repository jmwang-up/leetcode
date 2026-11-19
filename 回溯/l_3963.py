
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:


        res  = [[['#'] for _ in range(n)] for _ in range(m)]


        def back_strace(i, j):

            if i == m or j == n:
                return

            res[i][j] = '.'

            if j < n - 1:
                back_strace(i + 1, j)
            else:
                back_strace(i, j + 1)


        return [''.join([r for r in res])]