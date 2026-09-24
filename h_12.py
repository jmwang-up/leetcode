import sys


def solve():

    data = sys.stdin.read().strip()

    new_data = ''.join(c if  '0' <= c <= '9' else ' ' for c in data)
    data_list = new_data.split()
    max_len = max(len(part) for part in data_list)
    result = ''.join(sub_str for sub_str in data_list if len(sub_str) == max_len)
    print(f"{result}, {max_len}")
    

if __name__ == "__main__":

    solve()