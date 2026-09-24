import sys
from collections import Counter



def solve():

    data = sys.stdin.read().strip()
    count = Counter(data)
    for key, val in count.items():
        if val == 1:
            print(key)
            return
    print(-1)
    return
    
    

if __name__ == "__main__":

    solve()