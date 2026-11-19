from collections import Counter

class Solution:
    def minChanges(self, s: str) -> int:

        n = len(s)
        res = 0
        for i in range(0, n, 2):
            print(s[i:i+2])
            count = Counter(s[i:i+2])
            if count['1'] == 0 or count['0'] == 0:
                continue
            res += min(count['1'], count['0'])
        return res
            

if __name__ == "__main__":

    so = Solution()
    print(so.minChanges('1001'))
