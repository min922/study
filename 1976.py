# https://www.acmicpc.net/problem/1976
import sys
from collections import deque

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if tmp[j] == 1:
            graph[i].append(j + 1)
plan = list(map(int, sys.stdin.readline().split()))


def bfs(r):
    queue = deque([r])
    visited[r] = 1
    while queue:
        u = queue.popleft()
        for elt in graph[u]:
            if visited[elt] == 0:
                visited[elt] = 1
                queue.append(elt)


bfs(plan[0])
result = 1
for p in plan:
    if visited[p] == 0:
        result = 0
        break
if result == 1:
    print("YES")
else:
    print("NO")
