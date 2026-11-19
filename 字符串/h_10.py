import sys


def solve():

    data = sys.stdin.read().strip().split()
    print(' '.join(sub_str[::-1] for sub_str in data[::-1]))
        

if __name__ == "__main__":

    solve()