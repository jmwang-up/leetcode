import sys


def solve():

    data = sys.stdin.read().strip().split(';')

    def move(cmd, x, y, num):

        if cmd == 'A':
            x -= num
        elif cmd == 'S':
            y -= num
        elif cmd == 'D':
            x += num
        else:
            y += num

        return (x, y)

    x,y = 0, 0
    for cmds in data:
        cmd = cmds[0]
        num = cmds[1:]
        if not cmds:
            continue
        if cmd not in "ADWS":
            continue
        if not num.isdigit():
            continue
        if int(num) > 100 or int(num) < 0:
            continue

        x, y = move(cmd, x, y, int(num))

    print(x, y)
        

if __name__ == "__main__":

    solve()