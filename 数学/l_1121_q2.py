class Solution:
    def minRange(self, a: int, b: int, c: int) -> int:

  
        if a > b + c:
            a = b + c
        elif b > a + c:
            b = a + c
        elif c > a + b:
            c = a + b

        return max(a, b, c) - min(a,b,c)

if __name__ == "__main__":

    so = Solution()
    res = so.minRange(9, 2, 5)
    print(res)
    res = so.minRange(5, 7, 6)
    print(res)
    res = so.minRange(3, 3, 3)
    print(res)