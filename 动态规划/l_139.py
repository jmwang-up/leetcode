from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:


        self.memo = [-1] * len(s)

        def dp(s, start, wordDict):

            if start == len(s):
                return True

            if self.memo != -1:
                return self.memo[start] == 1

            for word in wordDict:

                length = len(word)

                if s[start:start + length] != word:
                    continue

                if dp(s, length + start, wordDict):
                    self.memo[start] = 1
                    return True

            self.memo[start] == 0
            return False

        return dp[0]

