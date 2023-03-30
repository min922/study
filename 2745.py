# https://www.acmicpc.net/problem/2745
import sys

tmp = sys.stdin.readline().split()
n, b = tmp[0], int(tmp[1])

result = 0
cnt = 0
for i in range(len(n)):
    dig = n[i]
    if dig.isdigit():
        result += (int(n[i])) * (b ** (len(n) - i - 1))
    else:
        result += (ord(n[i]) - 55) * (b ** (len(n) - i - 1))
print(result)
