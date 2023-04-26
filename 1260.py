# https://www.acmicpc.net/problem/1260
import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)  # 재귀 횟수 늘려주기


def dfs(r):
    visited_dfs[r] = True
    dfs_ans.append(r)
    graph[r].sort()
    for elt in graph[r]:
        if not visited_dfs[elt]:
            dfs(elt)


def bfs(r):
    visited_bfs[r] = True
    bfs_ans.append(r)
    queue = deque([r])
    while len(queue) != 0:
        u = queue.popleft()
        graph[u].sort()
        for elt in graph[u]:
            if not visited_bfs[elt]:
                visited_bfs[elt] = True
                bfs_ans.append(elt)
                queue.append(elt)


n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited_dfs = [False for _ in range(n + 1)]
visited_bfs = [False for _ in range(n + 1)]
bfs_ans = []
dfs_ans = []
dfs(v)
bfs(v)
print(*dfs_ans)
print(*bfs_ans)
