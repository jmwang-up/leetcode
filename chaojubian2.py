import sys


def solve():

    data = sys.stdin.read().split()
    n = int(data[0])
    a = [int(x) for x in data[1:1+n]]

    left = [0] * n
    stack = []

    for i in range(n):

        while stack and a[stack[-1]] <= a[i]:
            stack.pop()

        if stack:
            left[i] = stack[-1]
        else:
            left[i] = -1
        stack.append(i)

    right = [0] * n

    stack = []
    for i in range(n-1, -1, -1):

        while stack and a[stack[-1]] < a[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        else:
            right[i] = n

        stack.append(i)

    total = 0

    for i in range(n):
        cnt = (i - left[i]) * (right[i] - i)
        total += a[i] * cnt

    all_sub = n * (n + 1) // 2

    ans = total / all_sub
    print("{0:.6f}".format(ans))    


if __name__ == "__main__":

    solve()