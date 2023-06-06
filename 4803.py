# https://www.acmicpc.net/problem/4803
import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)


def find_cycle(start):
    # 시작노드부터 훑으면서 사이클 존재 여부를 return
    is_cycle = False
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if visited[u]: # 만약 이미 방문한 곳이라면 싸이클 존재
            is_cycle = True
        visited[u] = 1
        for elt in tree[u]:
            if visited[elt] == 0: # 방문하지 않았으면 큐에 추가
                queue.append(elt)
    return is_cycle


T = 1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if m == 0 and n == 0:
        break
    else:
        tree = [[] for _ in range(n + 1)]
        visited = [0 for _ in range(n + 1)]
        cnt = 0
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split())
            tree[a].append(b)
            tree[b].append(a)
        for node in range(1, n + 1):
            if visited[node] == 0:
                if not find_cycle(node):
                    cnt += 1
        if cnt == 0:
            print('Case {}: No trees.'.format(T))
        elif cnt == 1:
            print('Case {}: There is one tree.'.format(T))
        else:
            print('Case {}: A forest of {} trees.'.format(T, cnt))
        T += 1
