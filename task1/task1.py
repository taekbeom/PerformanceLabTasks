import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

cur = 1
while True:
    print(cur, end='')
    cur += (m - 1)

    if cur > n:
        cur -= n

    if cur == 1:
        break
