# https://www.acmicpc.net/problem/1463
import sys

x = int(sys.stdin.readline().strip())

dp = [0 for i in range(x + 1)]  # i까지 가기 위한 계산 횟수를 dp[i]에 저장

for i in range(2, x + 1):  # index 맞추기 위해 2부터
    dp[i] = dp[i - 1] + 1  # 그 전에서 다음으로 올 때 계산횟수 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # 최소 계산횟수 구하기 위해
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[-1])
