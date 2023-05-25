# https://www.acmicpc.net/problem/1956
import sys

v, e = map(int, sys.stdin.readline().split())
INF = 10e9
graph = [[INF for _ in range(v + 1)] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 1e9
for t in range(1, v + 1):
    # 싸이클은 출발지와 도착지가 같음
    ans = min(ans, graph[t][t])
if ans == 1e9:
    print(-1)
else:
    print(ans)
