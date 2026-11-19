import sys

def solve():

    data = sys.stdin.read().strip()
    n = len(data)

    def expand(left, right):

        while 0 <= left and right <= n and data[left] == data[right]:
            left -= 1
            right += 1

        return right - left - 1


    res = 0
    for i in range(n):
        res = max(res, expand(i, i), expand(i, i + 1))

    print(res)


if __name__ == "__main__":

    solve()