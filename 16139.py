# https://www.acmicpc.net/problem/16139
import sys

s = sys.stdin.readline().strip()
q = int(sys.stdin.readline().strip())

for i in range(q):
    t = list(sys.stdin.readline().split())
    a, l, r = t[0], int(t[1]), int(t[2])
    pre_sum = [0 for _ in range(len(s) + 1)]
    for j in range(len(s)):
        if s[j] == a:
            pre_sum[j + 1] = pre_sum[j] + 1
        else:
            pre_sum[j + 1] = pre_sum[j]
    print(pre_sum[r + 1] - pre_sum[l])
