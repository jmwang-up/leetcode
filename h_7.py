import sys

from collections import Counter

def solve():

    data = sys.stdin.read().strip()
    count = Counter(data)
    min_count = min(count.values())

    result = ''.join(c for c in data if count[c] > min_count)
    print(result)

if __name__ == "__main__":
    solve()