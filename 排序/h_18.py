import sys

def solve():

    data = sys.stdin.read().strip()

    print(''.join(sorted(data, key=lambda x:ord(x))))


if __name__ == "__main__":

    solve()