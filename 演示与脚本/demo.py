
# n = 10
s = '123456789'
# k = 3
# n = len(s)
# for i in range(0, n, k):
#     print(s[i:i+3])

print(list(map(int, s)))
for i in map(int, s):
    print(i)