import sys


def solve():

    data = sys.stdin.read().strip().split()
    string = data[0]
    k = int(data[1])
    print(string[:k])


if __name__ == "__main__":

    solve()