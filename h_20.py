import sys


def solve():

    data = sys.stdin.read().strip().split()
    n = int(data[0])
    k = int(data[-1])
    words = data[1: 1 + n]
    x = data[-2]
    # print(f"{ss}, {list(x)}")


    brothers = []

    for word in words:
        if word != x and sorted(word) == sorted(x):
            brothers.append(word)

    brothers.sort()
    print(len(brothers))

    if k <= len(brothers):
        print(brothers[k - 1])


if __name__ == "__main__":
    

    solve()
