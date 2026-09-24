import sys


def solve():

    data = sys.stdin.read().strip().split()

    s = data[0]
    t = data[1]

    print(transfrom(s, 1))
    print(transfrom(t, -1))


def transfrom(text, step):

    res = []

    for c in text:

        if '0' <= c <= '9':
            char = str((int(c) + 10 + step) % 10)
            res.append(char)
        elif 'A' <= c <= 'Z':
            index = (ord(c) - ord('A') + step) % 26
            res.append(chr(ord('a') + index))
        else:
            index = (ord(c) - ord('a') + step) % 26
            res.append(chr(ord('A') + index))

    return ''.join(res)



if __name__ == "__main__":

    solve()
