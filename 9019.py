# https://www.acmicpc.net/problem/9019
import sys
from collections import deque


def bfs(a, b):
    visited = [False for _ in range(10001)]
    queue = deque()
    queue.append([a, ''])
    visited[a] = True
    while queue:
        num, cmd = queue.popleft()
        if num == b:
            return cmd
        D = num * 2 % 10000
        if not visited[D]:
            visited[D] = True
            queue.append([D, cmd + "D"])
        S = 9999 if num == 0 else num - 1
        if not visited[S]:
            visited[S] = True
            queue.append([S, cmd + "S"])
        L = (num % 1000) * 10 + num // 1000
        if not visited[L]:
            visited[L] = True
            queue.append([L, cmd + "L"])
        R = (num % 10) * 1000 + num // 10
        if not visited[R]:
            visited[R] = True
            queue.append([R, cmd + "R"])


T = int(sys.stdin.readline().strip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(bfs(A, B))
