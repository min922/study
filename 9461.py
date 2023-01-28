# https://www.acmicpc.net/problem/9461
import sys

T = int(sys.stdin.readline().strip())

dp = [0 for _ in range(100)]

dp[0], dp[1], dp[2] = 1, 1, 1  # 초깃값

for i in range(T):
    N = int(sys.stdin.readline().strip())
    if dp[N - 1]:  # dp값이 저장되어있다면 print
        print(dp[N - 1])
    else:
        for j in range(3, N):
            dp[j] = dp[j - 3] + dp[j - 2]
        print(dp[N - 1])
