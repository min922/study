# https://www.acmicpc.net/problem/1167
import sys
from collections import deque

v = int(sys.stdin.readline().strip())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    tmp = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(tmp) - 1, 2):
        graph[tmp[0]].append([tmp[i], tmp[i + 1]])


def bfs(r):
    visited = [-1 for _ in range(v + 1)]
    radius, node = -1, -1
    queue = deque([r])
    visited[r] = 0
    while queue:
        u = queue.popleft()
        for i, d in graph[u]:
            if visited[i] == -1:
                visited[i] = visited[u] + d
                queue.append(i)
                if visited[i] > radius:
                    radius, node = visited[i], i
    return [radius, node]


_, n = bfs(1)  # 임의의 노드에서 가장 멀리 있는 노드 구한 후
rad, _ = bfs(n)  # 해당 노드와 가장 멀리 있는 노드사이의 거리가 지름
print(rad)
