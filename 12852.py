# https://www.acmicpc.net/problem/12852
import sys

n = int(sys.stdin.readline().strip())

dp = [[0, []] for _ in range(n + 1)]
# dp[i] = [i를 만드는 연산 횟수, 방법에 포함된 수]
dp[1] = [0, [1]]

for i in range(2, n + 1):
    dp[i][0] = dp[i - 1][0] + 1
    dp[i][1] = dp[i - 1][1] + [i]
    if i % 2 == 0:  # 2로 나누어떨어질 경우
        if dp[i][0] > dp[i // 2][0] + 1:  # 최소이면
            dp[i][0] = dp[i // 2][0] + 1  # 값 바꿔줌
            dp[i][1] = dp[i // 2][1] + [i]
    if i % 3 == 0:
        if dp[i][0] > dp[i // 3][0] + 1:
            dp[i][0] = dp[i // 3][0] + 1
            dp[i][1] = dp[i // 3][1] + [i]
print(dp[n][0])
print(*reversed(dp[n][1]))
