# https://www.acmicpc.net/problem/19532
import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())

ans = []
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c:
            ans.append([x, y])

for i in ans:
    x, y = i[0], i[1]
    if d * x + e * y == f:
        print(x, y)
