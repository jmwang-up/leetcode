import sys


def solve():

    data = sys.stdin.read().strip()
    one_nums = 0
    second_nums = 0
    num_nums = 0
    other_nums = 0
    for c in data:
        if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
            one_nums += 1
        elif ord(c) == 32:
            second_nums += 1
        elif 48 <= ord(c) <= 57:
            num_nums += 1
        else:
            other_nums += 1


    for i in [one_nums, second_nums, num_nums, other_nums]:
        print(i)


if __name__ == "__main__":
    solve()