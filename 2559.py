# https://www.acmicpc.net/problem/2559
import sys

n, k = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))
pre_sum = [0 for _ in range(n + 1)]

for i in range(n):
    pre_sum[i + 1] = pre_sum[i] + temp[i]
max_temp = -10000000
for i in range(n - k + 1):
    tmp = pre_sum[i + k] - pre_sum[i]  # i, k = 0, 2일 경우 pre[2]-pre[0]
    if tmp >= max_temp:  # list에 저장후 max()이용시 O(n)의 cost
        max_temp = tmp
print(max_temp)
