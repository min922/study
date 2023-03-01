# https://www.acmicpc.net/problem/10986
import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
presum = [0 for _ in range(n + 1)]
count = [0 for _ in range(m)]
for i in range(n):
    presum[i + 1] = (num[i] + presum[i]) % m
    count[presum[i + 1]] += 1
cnt = count[0]
for i in count:
    cnt += i * (i - 1) // 2  # 나머지 같은 것끼리 만들수있는 조합
print(cnt)
