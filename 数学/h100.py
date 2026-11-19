
while True:
    try:
        num = int(input())
        n = num
        sum = 0
        cur_num = 2
        while n > 0:
            sum += cur_num
            cur_num += 3
            n -= 1
    except:
        break

print(sum)