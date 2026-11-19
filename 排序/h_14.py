import sys

def solve():

    data = sys.stdin.read().strip().split()
    # n = int(data[0])

    res_data = data[1:]
    res_data.sort()
    for s in res_data:
        print(s)

if __name__ == "__main__":

    solve()