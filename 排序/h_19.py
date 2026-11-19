import sys


def solve():

    s = sys.stdin.read().strip()

    letters = [c for c in s if c.isalpha()]
    letters.sort(key=lambda x:x.lower())

    result = []
    index = 0

    for c in s:
        if c.isalpha():
            result.append(letters[index])
            index += 1
        else:
            result.append(c)

    print(''.join(result))






if __name__ == '__main__':

    solve()