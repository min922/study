# https://www.acmicpc.net/problem/24480
import sys

sys.setrecursionlimit(10 ** 9) # 재귀 횟수 늘려주기


def dfs_rev(R):
    global cnt # 몇 번째로 방문했는지 세는 변수
    visited[R] = cnt # R을 cnt번째로 방문 했다고 표기
    graph[R].sort(reverse=True) # 내림차순 정렬
    for elt in graph[R]: # R과 연결된 그래프의 모든 점들에 대해
        if visited[elt] == 0: # 방문한적이 0번이면
            cnt += 1 # 방문 횟수 늘리고
            dfs_rev(elt) # elt점에 대해 탐색 시작


n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 1
visited = [0 for _ in range(n + 1)]
dfs_rev(r)
for i in range(1, n+1):
    print(visited[i])
