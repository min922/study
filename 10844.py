# https://www.acmicpc.net/problem/10844
import sys

n = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1  # n이 1일 때 가능한 경우의 수
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n]) % 1000000000)
