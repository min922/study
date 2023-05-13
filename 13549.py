# https://www.acmicpc.net/problem/13549
import sys
from collections import deque


def bfs(start, end):
    queue = deque([start])
    visited = [-1 for _ in range(100001)]
    visited[start] = 0
    while queue:
        u = queue.popleft()
        if u == end:
            return visited[u]
        if 0 <= u - 1 < 100001 and visited[u - 1] == -1:
            visited[u - 1] = visited[u] + 1  # 걸을땐 1초
            queue.append(u - 1)
        if 0 < 2 * u < 100001 and visited[2 * u] == -1:
            visited[2 * u] = visited[u]  # 순간이동 0초
            queue.appendleft(2 * u)  # 순간이동 우선순위 높히기 위해
        if 0 <= u + 1 < 100001 and visited[u + 1] == -1:
            visited[u + 1] = visited[u] + 1
            queue.append(u + 1)


n, k = map(int, sys.stdin.readline().split())
print(bfs(n, k))
