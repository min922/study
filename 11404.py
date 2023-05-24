# https://www.acmicpc.net/problem/11404
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
INF = 10e9
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:  # 자기자신으로 가는 비용 0으로 초기화
            graph[i][j] = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(c, graph[a][b])

# 모든 정점에 대해 최소비용 계산 -> 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])  # 경유하는 비용이 더 적으면 갱신

for row in graph[1:]:
    for col in row[1:]:
        if col == INF:
            print(0, end=' ')
        else:
            print(col, end=' ')
    print('')
