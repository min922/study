# https://www.acmicpc.net/problem/11659
import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
pre_sum = [0 for _ in range(n + 1)]
for i in range(n):
    pre_sum[i + 1] = pre_sum[i] + num[i]  # 미리 부분합 구하기
for t in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(pre_sum[j] - pre_sum[i - 1])
