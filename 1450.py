# https://www.acmicpc.net/problem/1450
import sys
from itertools import combinations

n, c = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))
left_w = weight[:n // 2]
right_w = weight[n // 2:]
left_sum = []
right_sum = []
cnt = 0

# 반으로 나눠서 조합들의 합 전부 구함
for i in range(len(left_w) + 1):
    left_comb = combinations(left_w, i)
    for comb in left_comb:
        left_sum.append(sum(comb))
left_sum.sort()
for i in range(len(right_w) + 1):
    right_comb = combinations(right_w, i)
    for comb in right_comb:
        right_sum.append(sum(comb))

for r in right_sum:
    if r > c:
        continue
    # r에 대해서 이분탐색 진행
    start, end = 0, len(left_sum) - 1
    while start <= end:
        mid = (start + end) // 2
        if left_sum[mid] + r > c:
            end = mid - 1
        else:
            start = mid + 1
    cnt += (end + 1)  # end보다 작은 원소들은 전부 r과 더했을때 c보다 작음
print(cnt)
