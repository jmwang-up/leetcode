import sys

def solve():

    data = sys.stdin.read().strip().split()
    s = data[0]
    t = data[1]
    
    print('true' if set(s) <= set(t) else 'false')

if __name__ == "__main__":

    solve()