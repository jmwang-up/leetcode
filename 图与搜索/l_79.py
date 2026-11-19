class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])

        self.found = False

        def dfs(i, j, p):

            if p == len(word):
                self.found = True
                return


            if i < 0 or j < 0 or i == m or i == n:
                return

            if board[i][j] != word[p]:
                return

            

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        dfs(0, 0, 0)
        return self.found