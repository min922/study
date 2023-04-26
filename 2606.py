# https://www.acmicpc.net/problem/2606
import sys
from collections import deque


def net(r):
    global cnt
    visited[r] = True
    queue = deque([r])
    while len(queue) != 0:
        u = queue.popleft()
        for elt in graph[u]:
            if not visited[elt]:
                visited[elt] = True
                queue.append(elt)
                cnt += 1


n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(n + 1)]
cnt = 0
net(1)
print(cnt)
