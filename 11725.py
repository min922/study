# https://www.acmicpc.net/problem/11725
import sys
sys.setrecursionlimit(10**6)


def dfs(r):
    # r에 대해서 깊이우선탐색하면 r의 자식 노드들 찾을 수 있음
    for i in graph[r]:
        if visited[i] == 0:
            visited[i] = r
            dfs(i)


n = int(sys.stdin.readline().strip())

graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)  # 루트노드가 1
for i in range(2, n + 1):
    print(visited[i])
