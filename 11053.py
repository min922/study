# https://www.acmicpc.net/problem/11053
import sys

n = int(sys.stdin.readline().strip())

seq = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(n)]  # seq[i]까지로 만들 수 있는 부분수열의 크기 저장
for i in range(n):
    for j in range(i):
        if seq[i] > seq[j] and dp[i] < dp[j]:  # seq가 증가하고 부분수열의 크기가 최대가 아닐 때
            dp[i] = dp[j]
    dp[i] += 1  # seq[i]까지 포함하니까 1 증가
print(max(dp))
