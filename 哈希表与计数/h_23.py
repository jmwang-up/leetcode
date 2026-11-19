import sys

def solve():

    data = sys.stdin.read().strip().split()

    for s in data[1:]:
        print(count_satisfaction(s))


def count_satisfaction(s):

    from collections import Counter
    res = 0
    init_stat = 26
    c_count = list(Counter(s).values())
    c_count.sort(reverse=True)
    for times in c_count:
        res += init_stat * times
        init_stat -= 1

    return res





if __name__ == "__main__":
    solve()