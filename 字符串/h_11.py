import sys


def solve():

    data = sys.stdin.read().strip()
    res = 0
    for c in data:
        if 'A' <= c <= 'Z':
            res += 1
    print(res) 
        

if __name__ == "__main__":

    solve()