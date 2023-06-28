# https://www.acmicpc.net/problem/9372
import sys
from collections import deque


def bfs(r):
    queue = deque([r])
    visited[r] = 1
    cnt = 0
    while queue:
        u = queue.popleft()
        for elt in graph[u]:
            if visited[elt] == 0:
                visited[elt] += 1
                cnt += 1
                queue.append(elt)
    return cnt


T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    print(bfs(1))
