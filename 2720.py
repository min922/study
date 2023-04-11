# https://www.acmicpc.net/problem/2720
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    give = []
    coin = [25, 10, 5, 1]
    c = int(sys.stdin.readline().strip())
    for i in coin:
        tmp = divmod(c, i)
        give.append(tmp[0])
        c = tmp[1]
    print(*give)
