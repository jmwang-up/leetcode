import sys


def solve():

    data = sys.stdin.read().strip().split()
    s = data[0]
    t = data[1]

 
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    print(dict.fromkeys(s + alphabet))
    new_alphabet = ''.join(dict.fromkeys(s + alphabet))

    table = str.maketrans(alphabet, new_alphabet)
    print(table)
    print(t.translate(table))





if __name__ == "__main__":

    solve()