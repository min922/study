# https://www.acmicpc.net/problem/14002
import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n + 1)]

for i in range(n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j] + 1)
x = max(dp)
print(x)

result = []
for i in range(n - 1, -1, -1):
    if dp[i] == x:
        result.append(data[i])
        x -= 1
print(*reversed(result))
