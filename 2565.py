# https://www.acmicpc.net/problem/2565
import sys

n = int(sys.stdin.readline().strip())
line = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
line.sort()
# B 중 증가하는 부분수열을 구해야함 -> 그래야지 전깃줄 겹치지 않음
seq = [l[1] for l in line]
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))
