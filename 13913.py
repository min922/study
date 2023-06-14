# https://www.acmicpc.net/problem/13913
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
MAX = 100001
visited = [0 for _ in range(MAX)]
path = [0 for _ in range(MAX)]
result = []


def bfs(start, end):
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u == end:
            tmp = u
            while tmp != start:
                result.append(tmp)
                tmp = path[tmp]  # path를 되돌아가면서 저장
            result.append(start)
            return visited[u]
        for elt in (u - 1, u + 1, 2 * u):
            if 0 <= elt < MAX and visited[elt] == 0:
                visited[elt] = visited[u] + 1
                queue.append(elt)
                path[elt] = u  # 이전위치가 어디었는지 저장


print(bfs(n, k))
print(*reversed(result))
