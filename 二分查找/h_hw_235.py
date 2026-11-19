import sys


def solve():

    data = sys.stdin.read().strip().split()
    B = int(data[0])
    C = int(data[1])
    F = int(data[2])
    U = int(data[3])
    n = int(data[4])

    heights = list(map(int, data[5:5+n]))

    def check(H):
        T = 0
        for x in heights:
            if H > x:
                T += H - x

        if T == 0:
            return True

        cars = (T + C - 1) // C
        costs = cars * F + T * U
        # print(f"cost:{costs}->{H}")
        return costs <= B

    left = min(heights)
    right = max(heights) + B // U + 1

    while left < right:
        mid = (right + left) // 2
        # print(left, right, mid)
        # 预算足够, 找第一个不满足的
        if check(mid):
            left = mid + 1
        else:
            right = mid

    print(left - 1)



if __name__ == "__main__":
    solve()