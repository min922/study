# https://www.acmicpc.net/problem/1725
import sys

n = int(sys.stdin.readline().strip())
data = [int(sys.stdin.readline().strip()) for _ in range(n)]
data.append(0)

result = 0
stack = [(0, data[0])]
left = 0

for i in range(1, n + 1):
    left = i
    while stack and stack[-1][1] > data[i]:
        left, h = stack.pop()
        result = max(result, (i - left) * h)
    stack.append((left, data[i]))

print(result)
