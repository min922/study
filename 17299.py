# https://www.acmicpc.net/problem/17299
import sys

n = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))
f = {}
for number in num:
    if number not in f:
        f[number] = 1
    else:
        f[number] += 1

result = [-1] * n
stack = []

for i in range(n):
    while stack and f[stack[-1][0]] < f[num[i]]:
        tmp, idx = stack.pop()
        result[idx] = num[i]
    stack.append([num[i], i])
print(*result)
