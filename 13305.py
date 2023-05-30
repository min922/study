# https://www.acmicpc.net/problem/13305
import sys

n = int(sys.stdin.readline().strip())
length = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))
result = length[0] * cost[0]  # 첫번째 도시에서 무조건 주유
dist = 0
m = cost[0]
for i in range(1, n - 1):
    if cost[i] < m:  # 더 싸면
        result += m * dist  # 주유
        dist = length[i]
        m = cost[i]
    else:
        dist += length[i]  # 비싸면 지나가기
    if i == n - 2:  # 마지막도시
        result += m * dist
print(result)
