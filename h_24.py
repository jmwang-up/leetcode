import sys


def solve():
    
    data = sys.stdin.read().strip().split()

    s = data[0]
    k = int(data[1])

    left = 0
    right = 0

    n = len(s)

    gc_count = 0
    max_count = 0

    while right < n:

        if s[right] in 'GC':
            gc_count += 1

        right += 1

        if right - left == k:

            if gc_count > max_count:
                max_count = gc_count
                res = s[right - k: right]

            if s[left] in 'GC':
                gc_count -= 1
            left += 1
        
            
    print(res)

if __name__ == "__main__":
    solve()