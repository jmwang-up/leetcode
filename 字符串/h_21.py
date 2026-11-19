import sys

def solve():

    data = sys.stdin.read().strip().split()
    s = data[0]
    t = data[1]

    if len(s) > len(t):
        s, t = t, s

    n = len(s)

    # s 是短字符串, t是长字符串

    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            sub = s[start:start + length]

            if sub in t:
                print(sub)
                return

    print("")






if __name__ == "__main__":

    solve()