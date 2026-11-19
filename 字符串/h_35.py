import sys

def solve():

    data = sys.stdin.read().strip().split()

    bin_str = ''
    for sub_ip in data[0].split('.'):
        bin_str += format(int(sub_ip), "08b")
    print(int(bin_str, 2))

    second_bin_str = format(int(data[1]), "032b")


    i = 0
    res = []
    while i < len(second_bin_str):
        res.append(str(int(second_bin_str[i:i+8], 2)))
        i += 8

    print('.'.join(res))




if __name__ == "__main__":

    solve()